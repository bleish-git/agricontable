from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import date, datetime
from  anag_utenti.models import AnagraficaUtenti 
from django.utils.safestring import mark_safe
from django.utils.html import format_html
#from organizations.models import Organization, OrganizationUser


#class Account(Organization):
#    class Meta:
 #       proxy = True
 #       verbose_name = "Account"
 #       verbose_name_plural = "Accounts"


#class AccountUser(OrganizationUser):
#    class Meta:
 #       proxy = True
#        verbose_name = "Utente di Sistema"
  #      verbose_name_plural = "Utenti di Sistema"

class ContoCOGE (MPTTModel):    
    nome = models.CharField(max_length=2,default='')
    descrizione = models.CharField("Descrizione",max_length=50,default='')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nome']

    class Meta: 
        verbose_name = "Conto"
        verbose_name_plural = "Conti"

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
        return tmp + self.nome 
    __str__.allow_tags = True

        #for i in self.get_ancestors():
        #    tmp += i.nome + '.'
        #tmp += self.nome
        #return tmp + " - " + self.descrizione


        
    

class TipiDocCoge (models.Model):
    codDoc = models.CharField('Codice Documento', max_length=4,default='',blank=False)
    DesDoc = models.CharField('Descrizione',max_length=30)
    #inserire puntatore a lista di opzioni collegati ad operazioni ammesse al tipo documento

    class Meta: 
        verbose_name = "Tipo di Documento di contabilità"
        verbose_name_plural = "Tipi di Documento di contabilità"

    def __str__(self):
        return str(self.codDoc) + " - " + self.DesDoc
    

class PncGen (models.Model):
    tipoDoc = models.ForeignKey(TipiDocCoge,on_delete=models.CASCADE,blank=False)
    dataCreazionePnc = models.DateField('Data di Creazione',default=date.today, editable=False)
    numPnc = models.CharField('Numero Nota', max_length=10,default='',blank=True)
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
    idPnc = models.ForeignKey(PncGen,on_delete=models.CASCADE) #puntatore alla testata
    idRiga = models.CharField('ID', max_length=10,default='',blank=True)
    # tipoRiga
    partitarioRiga = models.ForeignKey(AnagraficaUtenti,on_delete=models.CASCADE,blank=True, null=True)
    descrizioneRiga = models.CharField('Descrizione', max_length=50,default='', blank=True)
    conto = models.ForeignKey(ContoCOGE,on_delete=models.CASCADE,blank=True, null=True) # puntatore al conto COGE
    dare = models.DecimalField(max_digits=16, decimal_places=5,blank=True, null=True)
    avere = models.DecimalField(max_digits=16, decimal_places=5,blank=True, null=True)
    competenzaDa = models.DateField('Competenza da',  default=date.today)
    competenzaA =  models.DateField('Competenza A', default=datetime.strptime('31/12/2099', '%d/%m/%Y'))

    #timestamp e variazioni con indicazione utentee

    class Meta: 
        verbose_name = "Riga"
        verbose_name_plural = "Righe"
    
class PncTes (models.Model):
    # stato = models.CharField('Stato', max_length=30,default='',blank=True)
    # dataCreazione = models.DateField('Data di inserimento',default=date.today)
    # tipoDoc = models.ForeignKey(TipiDoc,on_delete=models.CASCADE,blank=False)
    # #timestamp e variazioni con indicazione utentee  
    pass
