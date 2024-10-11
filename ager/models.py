from django.db import models

from django.db import models
from datetime import date, datetime
from multigroup.models import Gruppo, GruppoUser


class coltura (models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    nome = models.CharField('Coltura',blank=False)
    specie = models.CharField('Coltura',blank=False)
    varieta = models.CharField('Varietà',blank=True)
    descrizione = models.CharField('Descrizione',max_length=30)
    #

    class Meta: 
        verbose_name = "Coltura"
        verbose_name_plural = "Colture"

    def __str__(self):
        return str(self.nome) + " - " + self.descrizione

class certificazione (models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    nome = models.CharField('Certificazione',blank=False)
    descrizione = models.CharField('Descrizione',max_length=30)
    #

    class Meta: 
        verbose_name = "Certificazione"
        verbose_name_plural = "Certificazioni"

    def __str__(self):
        return str(self.nome) + " - " + self.descrizione


class fondo(models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    denominazione = models.CharField('Denominazione',blank=False)
    dettaglio = models.OneToOneField('Superfice')
    coltura = models.ForeignKey(coltura, on_delete=models.CASCADE)
    certificazione = models.ForeignKey(certificazione, on_delete=models.CASCADE)
    #



