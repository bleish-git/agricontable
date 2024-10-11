from django.db import models
from datetime import date
from multigroup.models import Gruppo

class CategorieUtente(models.Model): 
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    codiceCategoriaUtente = models.CharField("Categoria Utente",max_length=10)
    descrizioneCategoriaUtente = models.CharField("Descrizione",max_length=30)
    noteCategoriaUtente = models.CharField("Note",max_length=50,blank=True)

    def __str__(self):
        return self.descrizioneCategoriaUtente

    class Meta: 
        verbose_name = "Categoria Utente"
        verbose_name_plural = "Categorie Utenti"


class TipiUtente(models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    codiceTipoUtente = models.CharField("Tipo Utente",max_length=10)
    descrizioneTipoUtente = models.CharField("Descrizione",max_length=30)
    noteTipoUtente = models.CharField("Note",max_length=50,blank=True)
    
    def __str__(self):
        return self.descrizioneTipoUtente

    class Meta: 
        verbose_name = "Tipo Utente"
        verbose_name_plural = "Tipi Utenti"


class AnagColtura(models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    codiceTipoColtura = models.CharField("Codice Tipo Coltura",max_length=10)
    DescrColtura = models.CharField("Descrizione",max_length=30)
    NoteColtura = models.CharField("Note",max_length=50,blank=True)

    class Meta: 
        verbose_name = "Anagrafica Colture"
        verbose_name_plural = "Anagrafiche Colture"

    def __str__(self):
        return self.DescrColtura


class AnagraficaUtenti(models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE, related_name='anagraficautenti_gruppo')
    codice = models.IntegerField("Codice")
    cognome = models.CharField("Ragione sociale/Cognome",max_length=50)
    nome = models.CharField("Nome",max_length=50, blank=True)
    dataNascita = models.DateField("Data di nascita", blank=True)
    luogodinascita = models.CharField('Luogo di nascita',max_length=30,default='', blank=True)
    cf = models.CharField("Codice Fiscale",max_length=16,blank=True)
    piva = models.CharField("P.IVA",max_length=25,default='',blank=True)
    email =  models.CharField("email",max_length=50,default='',blank=True)
    pec = models.CharField("pec",max_length=50,default='',blank=True)
    tel = models.CharField("Telefono",max_length=20,default='',blank=True)
    cell = models.CharField("Cellulare",max_length=20,default='',blank=True)
    sdi = models.CharField('Codice Univoco SDI',max_length=10,default='',blank=True)
    iban = models.CharField('IBAN',max_length=30,default='',blank=True)
    indirizzo = models.CharField('Indirizzo',max_length=50,default='',blank=True)
    cap = models.CharField('CAP',max_length=6,default='',blank=True)
    citta = models.CharField('Città',max_length=30,default='',blank=True)
    prov = models.CharField('Prov',max_length=30,default='',blank=True)
    stato = models.CharField('Stato', max_length=30,default='',blank=True)
    datacreazione = models.DateField('Data di inserimento',default=date.today)
    categoriaUtente = models.ForeignKey(CategorieUtente,on_delete=models.CASCADE,blank=True)
    tipoUtente = models.ForeignKey(TipiUtente,on_delete=models.CASCADE,blank=True)

    class Meta: 
        verbose_name = "Anagrafica Utente"
        verbose_name_plural = "Anagrafiche Utenti"

    def save(self, *args, **kwargs):
        self.cognome = self.cognome.upper()
        self.nome = self.nome.upper()
        self.luogodinascita = self.luogodinascita.upper()
        self.cf = self.cf.upper()
        self.piva = self.piva.upper()
        self.sdi = self.sdi.upper()
        self.iban = self.iban.upper()
        self.citta = self.citta.upper()
        self.prov = self.prov.upper()
        self.stato = self.stato.upper()
        self.email = self.email.lower()
        self.pec = self.pec.lower()

        super().save(*args, **kwargs)

    def RagioneSociale(self):
        return + self.cognome + " " + self.nome

    def __str__(self):
        return str(self.codice) + " - " + self.cognome + " " + self.nome



    









