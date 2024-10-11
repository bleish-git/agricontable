from django.contrib import admin
from .models import Gruppo, GruppoUser, GruppoOwner, GruppoInvitation, Profilo
from django.contrib.auth.models import User
from django import forms 
from lib.checkfielddata import controllaCF, controllaPIVA
from django.db.models import Max
from organizations import models
from django.forms.models import BaseInlineFormSet
from django.urls import resolve


class UserInline(admin.TabularInline):
    model = GruppoUser
    #formset = UserInlineFormset
    extra = 1
    #autocomplete_fields = ['user']

    def get_queryset(self, request):
        qs = super(UserInline, self).get_queryset(request)
        return qs.filter(organization_id=int(resolve(request.path_info).kwargs['object_id']))

    class Meta:
        verbose_name_plural = "Lista utenti"


class PostForm(forms.ModelForm):
    def get_queryset(request):
        qs = super().get_queryset(request)
        if hasattr(request, 'session'):
            return qs.filter(gruppo=int(request.session['gruppo_utente']))
        return qs


    def clean(self):

        result = {'cf': controllaCF(self.cleaned_data['cf']), 'piva': controllaPIVA(self.cleaned_data['piva'])}
        nuovo_result ={}

        for chiave, valore in result.items():
            if valore:
                nuovo_result[chiave] = valore
        if nuovo_result:
            raise forms.ValidationError(nuovo_result)



@admin.register(Gruppo)
class GruppoAdmin(admin.ModelAdmin): 
    form = PostForm
    inlines = [UserInline]
    ordering = ['nomeEsteso']
    list_display = ('name','nomeEsteso','is_active')
    list_filter = ('nomeEsteso',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(request, 'organization'):
            return qs.filter(id=int(request.organization.id))
        return qs

@admin.register(GruppoUser)
class GruppoUserAdmin(admin.ModelAdmin):
    list_display = ('organization','user','nomecompleto',)
    list_filter = ('user','organization',)
    filter_horizontal = ['permission',]
    fields = (('organization','gruppo_predefinito'),('user','user_type','is_admin'), 'permission')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(request, 'gruppo'):
            return qs.filter(organization_id=int(request.organization.id))
        return qs



@admin.register(GruppoOwner)
class GruppoOwnerAdmin(admin.ModelAdmin):
    list_display = ('organization_user','organization',)


@admin.register(GruppoInvitation)
class GruppoInvitationAdmin(admin.ModelAdmin):
    pass


#TODO inserire filtro delle app non presenti nelle associazioni utenti-gruppi

#admin.site.register(Gruppo,GruppoAdmin)

#Per rimuovere una app dalla lista app di django-admin; deve essere elencata prima della app che la
#chiama in settings
admin.site.unregister(models.Organization)
admin.site.unregister(models.OrganizationInvitation)
admin.site.unregister(models.OrganizationOwner)
admin.site.unregister(models.OrganizationUser)

