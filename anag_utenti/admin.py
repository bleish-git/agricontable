from django.contrib import admin

from .models import AnagraficaUtenti, CategorieUtente, TipiUtente, AnagColtura

admin.site.register(AnagraficaUtenti)

admin.site.register(CategorieUtente)
admin.site.register(TipiUtente)
admin.site.register(AnagColtura)
