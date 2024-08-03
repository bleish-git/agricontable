from django.contrib import admin
from .models import ContoCOGE,TipiDocCoge, PncGen, PncRighe
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html


#from organizations.models import Organization, OrganizationUser, OrganizationOwner
#from contable.models import Account, AccountUser



class ContoCOGEAdmin (DjangoMpttAdmin):
    list_display = ('antenati', 'get_description',)
    #ordering = ["nome"]
    search_fields = ["descrizione"]
    readonly_fields = ['antenati']
    autoescape = False

    def get_description(self, obj):
       return mark_safe(obj)
    get_description.short_description = 'Gerarchia'
    get_description.allow_tags = True

class PncRigheInline(admin.TabularInline):
    model = PncRighe
    autocomplete_fields = ['conto']
    class Meta:
        verbose_name_plural = "Corpo del documento"

class PncAdmin(admin.ModelAdmin):
    ordering = ['numPnc']
    list_display = ('numPnc','dataPnc')
    inlines = (PncRigheInline,)
    list_filter = ('esercizioCompetenza',)
    search_fields = ['numPnc','tipoDocCoge']


admin.site.register(ContoCOGE,ContoCOGEAdmin)
admin.site.register(TipiDocCoge)
admin.site.register(PncGen,PncAdmin)
#admin.site.register(Account)
#admin.site.register(AccountUser)
