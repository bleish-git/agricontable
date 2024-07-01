from django.urls import path, re_path

from . import views

app_name = 'Anagrafica'

urlpatterns = [
    re_path("^index*", views.index, name="index"),
]
