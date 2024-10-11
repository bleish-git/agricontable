from django.contrib import admin
from .models import ContoCOGE,TipiDocCoge, PncGen, PncRighe
from multigroup.models import GruppoUser
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import forms 
from django.contrib.auth.models import User
#from django.utils.functional import curry


class postForm(forms.ModelForm):
    view_on_site = False

    class Meta:
        model = ContoCOGE
        fields ='__all__'
        widgets = {
            'gruppo': forms.widgets.HiddenInput()
        }
            

    # def clean_gruppo(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.gruppo
    #     else:
    #         return self.cleaned_data['gruppo']
    
    def clean(self):
        #caso in cui il gruppo attivo ha radici, ovvero non è il primo inserimento per il gruppo,
        #ma non viene indicato nel form il genitore, per cui occorre che non rimanga fluttuante
        alberi = ContoCOGE.objects.filter(parent=None).values_list('gruppo_id',flat=True)
        eer={}
        if 'parent' in self.cleaned_data and self.cleaned_data['parent'] is None and self.cleaned_data['gruppo'].id in alberi:
            eer['parent']='Indicare il livello superiore.'
        
        raise forms.ValidationError(eer)



@admin.register(ContoCOGE)
class ContoCOGEAdmin (DjangoMpttAdmin):

    form = postForm
    list_display = ('antenati', 'get_description',)
    #ordering = ["nome"]
    search_fields = ["descrizione"]
    readonly_fields = ['antenati']
    autoescape = False

    def filter_tree_queryset(self, queryset,request):
        qs = queryset.filter(gruppo_id=int(request.session['gruppo_utente']))
        num = len(qs)
        return qs
    
    def get_description(self, obj):
       return mark_safe(obj)
    get_description.short_description = 'Gerarchia'
    get_description.allow_tags = True


    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}



class PncRigheInline(admin.TabularInline):
    model = PncRighe
    search_fields = ['descrizione']
    autocomplete_fields = ['partitarioRiga','conto',]
    list_select_related = ('partitarioRiga','conto')
    extra = 1

    def filter_tree_queryset(self, queryset,request):
        qs = queryset.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'gruppo' or db_field.name == 'idRiga' or db_field.name == 'idPnc':
            kwargs['widget'] = forms.HiddenInput()

        if db_field.name == 'conto':

            db = kwargs.get("using")
            qs = self.get_field_queryset(db, db_field, request)
            db_field.choices = [ ( p.id, '{0}'.format( str(p)),) for p in qs.filter(gruppo_id = request.session['gruppo_utente']).exclude(parent=None) ]
            #db_field.choices=qs.filter(gruppo_id = request.session['gruppo_utente']).values_list('id','nome','descrizione')

        return super(PncRigheInline,self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        super(PncRigheInline, self).get_form(*args, **kwargs)
        self.fields['conto'].queryset = ContoCOGE.objects.filter(gruppo_id = request.session['gruppo_utente'])


@admin.register(PncGen)
class PncGenAdmin(admin.ModelAdmin):
    ordering = ['numPnc']
    list_display = ('numPnc','dataPnc', 'causalePnC')
    inlines = (PncRigheInline,)
    list_filter = ('esercizioCompetenza',)
    search_fields = ['numPnc','tipoDoc']

    def get_queryset(self, request):
        qs = super(PncGenAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {'gruppo': forms.widgets.HiddenInput()}
        a = super(PncGenAdmin,self).get_form(request, obj, **kwargs)
        a.base_fields['tipoDoc'].queryset = TipiDocCoge.objects.filter(gruppo_id=request.session['gruppo_utente'])
        return a


        

@admin.register(TipiDocCoge)
class TipiDocCogeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TipiDocCogeAdmin,self).get_queryset(request)
        if 'gruppo_utente' in request.session:
            qs=qs.filter(gruppo_id=int(request.session['gruppo_utente']))
        return qs

    def get_changeform_initial_data(self, request):
        return {'gruppo': int(request.session['gruppo_utente'])}

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {   'gruppo': forms.widgets.HiddenInput()}
        return super().get_form(request, obj, **kwargs)
