from . import views
from django.urls import path
from django.urls import re_path


urlpatterns = [ re_path("cambia_gruppo/", views.cambia_gruppo_modal, name="cambia_gruppo_modal"),
                re_path('setgroup/', views.set_gruppo, name='setgruppo'),
]

