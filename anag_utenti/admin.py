from django.contrib import admin

from .models import AnagraficaUtenti, CategorieUtente, TipiUtente, AnagColtura
from django import forms 
from lib.checkfielddata import controllaCF, controllaPIVA


class PostForm(forms.ModelForm):
    class Meta:
        model = AnagraficaUtenti
        fields ='__all__'
        widgets = {
            'gruppo': forms.widgets.HiddenInput()
        }

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
    search_fields = [""]
    autoescape = False

    def get_queryset(self, request):
        qs = super(AnagraficaUtentiAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}


@admin.register(CategorieUtente)
class CategorieUtenteAdmin(admin.ModelAdmin): 
    #list_display = ('__str__','cf')
    #search_fields = [""]
    autoescape = False

    def get_queryset(self, request):
        qs = super(CategorieUtenteAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = { 'gruppo': forms.widgets.HiddenInput() }
        return super().get_form(request, obj, **kwargs)


@admin.register(TipiUtente)
class TipiUtenteAdmin(admin.ModelAdmin): 
    #list_display = ('__str__','cf')
    #search_fields = [""]
    autoescape = False

    def get_queryset(self, request):
        qs = super(TipiUtenteAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = { 'gruppo': forms.widgets.HiddenInput() }
        return super().get_form(request, obj, **kwargs)

        
@admin.register(AnagColtura)
class AnagColturaAdmin(admin.ModelAdmin): 
    #list_display = ('__str__','cf')
    #search_fields = [""]
    autoescape = False

    def get_queryset(self, request):
        qs = super(AnagColturaAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = { 'gruppo': forms.widgets.HiddenInput() }
        return super().get_form(request, obj, **kwargs)


