from django.contrib import admin
from .models import ContoCOGE, PncGen
#from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

admin.site.register(ContoCOGE, DjangoMpttAdmin)
admin.site.register(PncGen)

#MPTT_ADMIN_LEVEL_INDENT = 20

