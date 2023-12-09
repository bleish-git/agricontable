from django.contrib import admin
from .models import ContoCOGE,TipiDocCoge, PncGen, PncRighe
#from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin



#MPTT_ADMIN_LEVEL_INDENT = 20

class PncRigheInline(admin.TabularInline):
    model = PncRighe
    class Meta:
        verbose_name_plural = "Corpo del documento"

class PncAdmin(admin.ModelAdmin):
    ordering = ['numPnc']
    list_display = ('numPnc','dataPnc')
    inlines = (PncRigheInline,)
    list_filter = ('esercizioCompetenza',)
    search_fields = ['numPnc','tipoDocCoge']



admin.site.register(ContoCOGE, DjangoMpttAdmin)
admin.site.register(TipiDocCoge)
admin.site.register(PncGen,PncAdmin)