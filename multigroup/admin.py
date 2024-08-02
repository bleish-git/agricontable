from django.contrib import admin

# from organizations.base_admin import (
#     BaseOwnerInline,
#     BaseOrganizationAdmin,
#     BaseOrganizationUserAdmin,
#     BaseOrganizationOwnerAdmin,
# )

from .models import Gruppo, GruppoUser, GruppoOwner, GruppoInvitation

class UserInline(admin.TabularInline):
    model = GruppoUser
    #autocomplete_fields = ['user']
    class Meta:
        verbose_name_plural = "Lista utenti"



@admin.register(Gruppo)
class GruppoAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    #ordering = ['numPnc']
    list_display = ('name','nomeEsteso',)
    #inlines = (PncRigheInline,)
    list_filter = ('nomeEsteso',)
    #search_fields = ['numPnc','tipoDocCoge']


@admin.register(GruppoUser)
class GruppoUserAdmin(admin.ModelAdmin):
    list_display = ('user','organization',)
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

