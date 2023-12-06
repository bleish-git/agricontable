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


class PncGen (models.Model):
    stato = models.CharField('Stato', max_length=30,default='',blank=True)
    datacreazione = models.DateField('Data di inserimento',default=date.today)
    categoriaUtente = models.ForeignKey(CategorieUtente,on_delete=models.CASCADE,blank=True)

    codice=0
    cognome=0
    nome=0

    class Meta: 
        verbose_name = "Prima nota contabile"
        verbose_name_plural = "Prime Note Contabili"

    def __str__(self):
        return str(self.codice) + " - " + self.cognome + " " + self.nome