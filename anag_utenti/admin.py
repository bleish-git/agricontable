from django.contrib import admin

from .models import AnagraficaUtenti, CategorieUtente, TipiUtente, AnagColtura
from django import forms 
from lib.checkfielddata import controllaCF, controllaPIVA


class PostForm(forms.ModelForm):
    def clean(self):

        result = {'cf': controllaCF(self.cleaned_data['cf']), 'piva': controllaPIVA(self.cleaned_data['piva'])}
        nuovo_result ={}

        for chiave, valore in result.items():
            if valore:
                nuovo_result[chiave] = valore
        if nuovo_result:
            raise forms.ValidationError(nuovo_result)

@admin.register(AnagraficaUtenti)
class AnagraficaUtentiAdmin(admin.ModelAdmin): 
    form = PostForm
    list_display = ('__str__','cf')



admin.site.register(CategorieUtente)
admin.site.register(TipiUtente)
admin.site.register(AnagColtura)
