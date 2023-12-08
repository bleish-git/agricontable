from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import date

class ContoCOGE (MPTTModel):    
    idContoCOGE = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=2)
    descrizione = models.CharField("Descrizione",max_length=20)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nome']

    class Meta: 
        verbose_name = "Conto"
        verbose_name_plural = "Conti"

    def __str__(self):
        return str(self.nome) + " - " + self.descrizione

class TipiDocCoge ():
    codDoc = models.CharField('Codice Documento', max_length=4,default='',blank=False)
    DesDoc = models.CharField('Descrizione',max_length=30)
    #inserire puntatore a lista di opzioni collegati ad operazioni ammesse al tipo documento

class PncGen (models.Model):
    idPnc = models.BigAutoField(primary_key=True, default=0)
    tipoDocCoge = models.ForeignKey(TipiDocCoge,on_delete=models.CASCADE,blank=False)
    dataPnc = models.DateField('Data Nota', blank=True)
    numPnc = models.CharFsield('Num. Nota', max_length=15,default='',blank=True)
    statoPnc = models.CharFsield('Stato', max_length=30,default='',blank=True) 
    dataCreazionePnc = models.DateField('Data di inserimento',default=date.today)
    #pncRiga = models.ForeignKey(PncRighe,on_delete=models.CASCADE,blank=False)
    pncRiga = models.ManyToManyField(PncRighe)
    #timestamp e variazioni con indicazione utentee

    class Meta: 
        verbose_name = "Prima nota contabile"
        verbose_name_plural = "Prime Note Contabili"

    def __str__(self):
        return str(self.idPnc) + " - " + self.tipoDoc


class PncRighe (model.Model):
    idPnc = models.BigAutoField(primary_key=True, default=0)
    stato = models.CharField('Stato', max_length=30,default='',blank=True)
    datacreazione = models.DateField('Data di inserimento',default=date.today)
    #tipoDoc = models.ForeignKey(TipiDoc,on_delete=models.CASCADE,blank=False)
    #timestamp e variazioni con indicazione utentee



class PncTes (model.Model):
    idPnc = models.BigAutoField(primary_key=True, default=0)
    stato = models.CharField('Stato', max_length=30,default='',blank=True)
    datacreazione = models.DateField('Data di inserimento',default=date.today)
    #tipoDoc = models.ForeignKey(TipiDoc,on_delete=models.CASCADE,blank=False)
    #timestamp e variazioni con indicazione utentee