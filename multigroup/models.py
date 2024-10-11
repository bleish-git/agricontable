from django.db import models
from datetime import date, datetime
from django.core.exceptions import ValidationError
from django.conf import settings

from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationUser,
    AbstractOrganizationOwner,
    AbstractOrganizationInvitation,
)

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

#l'utilizzo di thread.locals è sconsigliato
#per cui si è preferito utilizzare l'attributo session in request
""" class GruppoUserManager(models.Manager):
        
    def get_current_gruppo():
        from threading import local
        _local=local
        return getattr(_local, 'organization', None)

    def get_queryset(self):
        #return super(GruppoUserManager,self).get_query_set().filter(user_id=4)
        return super().get_queryset().filter(organization = int(self.get_current_gruppo))
 """

class GruppoUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

#In quel che segue, per Gruppo si intende un tenant o azienda
class Gruppo(AbstractOrganization):
    """Modello esteso di Organization, che eredita i suoi campi e aggiunge i seguenti"""
    #name= models.TextField("Sigla",max_length=5, blank=False, unique=True)
    nomeEsteso = models.TextField("Denominazione",max_length=35, blank=False)
    description = models.TextField("Descrizione")
    url = models.URLField("Sito web",blank=True)
    address = models.CharField("Indirizzo",max_length=30, blank=True)
    city = models.CharField("città",max_length=30, blank=True)
    cap = models.CharField("CAP",max_length=5, blank=True)
    cf = models.CharField("C.F.",max_length=20, blank=True)
    piva = models.CharField("P.IVA",max_length=20, blank=True)
     

    class Meta:
      verbose_name = "Organizzazione"
      verbose_name_plural = "Organizzazioni"
          
    def __str__(self):
        return str(self.nomeEsteso)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('name').verbose_name = 'Sigla'
        self._meta.get_field('is_active').verbose_name = "E' attivo?"

#Viene associata per ogni gruppo/azienda la relativa lista di utenti
class GruppoUser(AbstractOrganizationUser):
    USER_TYPE = {
    "GN": "Generic",
    "AD": "Admin",
    "GU": "Guest",
    }


    user_type = models.CharField("Categoria Utente",max_length=2,choices=USER_TYPE, default="GN")
    gruppo_predefinito = models.BooleanField("Predefinita per l'utente")
    permission = models.ManyToManyField(Permission, verbose_name='Abilitazioni')

    #objects = GruppoUserManager()

    class Meta:
        verbose_name = "Associazione Utenti ed Organizzazioni"
        verbose_name_plural = "Utenti dell'organizzazione"
        unique_together = ('user', 'organization')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('user').verbose_name = 'Utente'
        self._meta.get_field('organization').verbose_name = 'Organizzazioni'  
        self._meta.get_field('permission').verbose_name = 'Abilitazioni'   
    #    self._meta.get_field('nomecompleto').verbose_name = 'Utente'   

    def nomecompleto(self):
        return self.name

    def __str__(self):
        return str(self.nomecompleto())


class GruppoOwner(AbstractOrganizationOwner):

    class Meta:
      verbose_name = "Proprietari dell'Organizzazione "
      verbose_name_plural = "Proprietari delle Organizzazioni"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self._meta.get_field('user').verbose_name = 'Utente'
        #self._meta.get_field('organization').verbose_name = 'Gruppo'
        

    pass

class GruppoInvitation(AbstractOrganizationInvitation):
    pass



class Profilo(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username
