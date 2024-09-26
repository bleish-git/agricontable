from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.forms import TreeNodeChoiceField
from datetime import date, datetime
from anag_utenti.models import AnagraficaUtenti 
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from multigroup.models import Gruppo, GruppoUser
from django.contrib.auth.models import User


class TreeNodeChoiceFieldFiltered(TreeNodeChoiceField):
    def __init__(self, queryset, *args, **kwargs):
        _root = kwargs.pop('root', None)

        if _root is not None:
            pid = None
            for i in queryset:
                if i.root.name == _root:
                    pid = i.tree_id
                    break

            if pid is not None:
                queryset = queryset.filter(tree_id = pid) 

        super(TreeNodeChoiceFieldFiltered, self).__init__(queryset, *args, **kwargs)



class TreeForeignKeyFiltered(models.ForeignKey):
    #based on TreeForeignKeyfiltered on mptt module
    def __init__(self, *args, **kwargs):
        self._root = kwargs.pop('root', None)
        super(TreeForeignKeyFiltered, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.setdefault('root', self._root)
        kwargs.setdefault('form_class', TreeNodeChoiceFieldFiltered)
        return super(TreeForeignKeyFiltered, self).formfield(**kwargs)



class ContoCOGE (MPTTModel):  

    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE, related_name='contoCOCGE_gruppo')
    nome = models.CharField(max_length=2,default='')
    descrizione = models.CharField("Descrizione",max_length=50,default='')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nome']

    class Meta: 
        verbose_name = "Conto"
        verbose_name_plural = "Conti"
        constraints = [
            models.UniqueConstraint(fields=['gruppo', 'nome','parent'], name="unique_conto_del_gruppo"),
        ]

    def antenati(self):
        tmp=''
        if self.is_root_node():
            return  format_html(f'<b> {{}} - {{}} </b>', mark_safe(self.nome), mark_safe(self.descrizione))
        for i in self.get_ancestors():
            tmp += i.nome + '.'
        return tmp+self.nome+' - '+self.descrizione 

    antenati.allow_tags = True   

    def __str__(self):
        tmp=''
        if self.is_root_node():
            return  format_html(f'<b> {{}} - {{}} </b>', mark_safe(self.nome), mark_safe(self.descrizione))
        for i in self.get_ancestors():
            tmp += i.nome + '.'
        return tmp + self.nome + ' - '+self.descrizione
    __str__.allow_tags = True


    def clean(self):
        #Quando si crea un contoCOGE, verranno creati tanti alberi quanti i gruppi
        #ogni tree_id sarà impostato uguale al gruppo_id
        #Se la gerarchia dei contoCOGE per un determinato gruppo è vuota, ovvero manca il tree_id uguale,
        #ovvero, equivalentemente, è il primo inserimento per il gruppo attivo,
        #per quest'ultimo viene preventivamente creato il nodo radice 
        #(con tree_id=request.session['gruppo_utente']) e poi il conto che si sta salvando va inserito come figlio
        alberi = ContoCOGE.objects.filter(parent=None).values_list('gruppo_id',flat=True)

        #caso in cui il gruppo attivo non ha radici, ovvero è il primo inserimento per il gruppo,
        if self.gruppo_id not in alberi:
            nuovo_albero=ContoCOGE(gruppo=self.gruppo, tree_id=self.gruppo_id, nome='@', descrizione=str(self.gruppo).upper(),parent=None, level=0)
            nuovo_albero.save()
            self.parent = nuovo_albero
            self.tree_id= self.gruppo_id


class TipiDocCoge (models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    codDoc = models.CharField('Codice Documento', max_length=4,default='',blank=False)
    DesDoc = models.CharField('Descrizione',max_length=30)
    #inserire puntatore a lista di opzioni collegati ad operazioni ammesse al tipo documento

    class Meta: 
        verbose_name = "Tipo di Documento di contabilità"
        verbose_name_plural = "Tipi di Documento di contabilità"

    def __str__(self):
        return str(self.codDoc) + " - " + self.DesDoc
    

class PncGen (models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    tipoDoc = models.ForeignKey(TipiDocCoge,on_delete=models.CASCADE,blank=False)
    dataCreazionePnc = models.DateField('Data di Creazione',default=date.today, editable=False)
    numPnc = models.CharField('Numero Nota', max_length=10,default='',blank=False)
    dataPnc = models.DateField('Data del documento',default=date.today)
    esercizioCompetenza = models.CharField('Esercizio Contabile', max_length=4,default=str(datetime.now().year),blank=False)
    causalePnC = models.CharField('Causale', max_length=50,default='',blank=True)
    # # competenzaDa  =models.DateField('Competenza da',  default=date.today)
    # competenzaA =  models.DateField('Competenza A', default=datetime.strptime('31/12/2099', '%d/%m/%Y'))


    class Meta: 
        verbose_name = "Prima Nota Contabile"
        verbose_name_plural = "Prime Note Contabili"

    def __str__(self):
        return str(self.numPnc) + " - " + self.causalePnC


class PncRighe (models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    idPnc = models.ForeignKey(PncGen,on_delete=models.CASCADE) #puntatore alla testata
    #idRiga = models.CharField('ID', max_length=10,default='',blank=True)
    # tipoRiga
    partitarioRiga = models.ForeignKey(AnagraficaUtenti,on_delete=models.CASCADE,blank=True, null=True)
    descrizioneRiga = models.CharField('Descrizione', max_length=50,default='', blank=True)
    conto = TreeForeignKey(ContoCOGE,on_delete=models.CASCADE,blank=True, null=True) # puntatore al conto COGE
    dare = models.DecimalField(max_digits=16, decimal_places=5,blank=True, null=True)
    avere = models.DecimalField(max_digits=16, decimal_places=5,blank=True, null=True)
    competenzaDa = models.DateField('Competenza da',  default=date.today)
    competenzaA =  models.DateField('Competenza a', default=datetime.strptime('31/12/2099', '%d/%m/%Y'))

    #timestamp e variazioni con indicazione utentee

    class Meta: 
        verbose_name = "Riga"
        verbose_name_plural = "Righe"
    
class PncTes (models.Model):
    # gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    # stato = models.CharField('Stato', max_length=30,default='',blank=True)
    # dataCreazione = models.DateField('Data di inserimento',default=date.today)
    # tipoDoc = models.ForeignKey(TipiDoc,on_delete=models.CASCADE,blank=False)
    # #timestamp e variazioni con indicazione utentee  
    pass
