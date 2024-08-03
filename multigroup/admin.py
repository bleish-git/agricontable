from django.contrib import admin
from .models import Gruppo, GruppoUser, GruppoOwner, GruppoInvitation
from django import forms 
from lib.checkfielddata import controllaCF, controllaPIVA


class UserInline(admin.TabularInline):
    model = GruppoUser
    #autocomplete_fields = ['user']
    class Meta:
        verbose_name_plural = "Lista utenti"




class PostForm(forms.ModelForm):
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
    #ordering = ['numPnc']
    list_display = ('name','nomeEsteso','is_active')
    list_filter = ('nomeEsteso',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GruppoUser)
class GruppoUserAdmin(admin.ModelAdmin):
    list_display = ('user','nomecompleto','organization',)
    list_filter = ('user','organization',)

    pass


@admin.register(GruppoOwner)
class GruppoOwnerAdmin(admin.ModelAdmin):
    list_display = ('organization_user','organization',)
    pass

@admin.register(GruppoInvitation)
class GruppoInvitationAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Gruppo,GruppoAdmin)

