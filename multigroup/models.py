from django.db import models
from datetime import date, datetime
from django.core.exceptions import ValidationError

from django.db import models
from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationUser,
    AbstractOrganizationOwner,
    AbstractOrganizationInvitation,
)




class Gruppo(AbstractOrganization):
    """Modello esteso di Organization, che eredita i suoi campi e aggiunge i seguenti"""
    nomeEsteso = models.TextField("Denominazione",max_length=35, blank=False)
    description = models.TextField("Descrizione")
    url = models.URLField("Sito web",blank=True)
    address = models.CharField("Indirizzo",max_length=30, blank=True)
    city = models.CharField("città",max_length=30, blank=True)
    cap = models.CharField("CAP",max_length=5, blank=True)
    cf = models.CharField("C.F.",max_length=20, blank=True)
    piva = models.CharField("P.IVA",max_length=20, blank=True)
    #logo 

    class Meta:
      verbose_name = "Gruppo"
      verbose_name_plural = "Gruppi"
          
    def __str__(self):
        return str(self.nomeEsteso)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('name').verbose_name = 'Sigla'
        self._meta.get_field('is_active').verbose_name = "E' attivo?"

    
        


#Viene associata per ogni gruppo la relativa lista di utenti
class GruppoUser(AbstractOrganizationUser):
    USER_TYPE = {
    "GN": "Generic",
    "AD": "Admin",
    "GU": "Guest",
    }


    user_type = models.CharField("Categoria Utente",max_length=2,choices=USER_TYPE, default="GN")

    class Meta:
      verbose_name = "Associazione Utenti e Gruppi"
      verbose_name_plural = "Utenti del Gruppo"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('user').verbose_name = 'Utente'
        self._meta.get_field('organization').verbose_name = 'Gruppo'     
    #    self._meta.get_field('nomecompleto').verbose_name = 'Utente'   

    def nomecompleto(self):
        return self.name

    def __str__(self):
        return str(self.nomecompleto())

class GruppoOwner(AbstractOrganizationOwner):

    class Meta:
      verbose_name = "Proprietari dei Gruppi "
      verbose_name_plural = "Proprietari dei Gruppi"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self._meta.get_field('user').verbose_name = 'Utente'
        #self._meta.get_field('organization').verbose_name = 'Gruppo'
        

    pass

class GruppoInvitation(AbstractOrganizationInvitation):
    pass
