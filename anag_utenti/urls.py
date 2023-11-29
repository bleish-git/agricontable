from django.urls import path

from . import views

app_name = 'anagrafica'

urlpatterns = [
    path("", views.index, name="index"),
]