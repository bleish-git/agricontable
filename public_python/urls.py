"""
URL configuration for public_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from organizations.backends import invitation_backend
from registrationForm import views

#'from django.conf.urls.static import static' e '+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'
#sono aggiunti per il developmente con python manage.py runserver

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('info/', include('info.urls')),
        path('anag/', include('anag_utenti.urls')),
        path('accounts/', include('organizations.urls')),
        path('invitations/', include(invitation_backend().get_urls())),
        path('signup/', views.sign_up, name="signup"),
        path('login/', views.user_login, name='login'),
        path('profile/', views.user_profile, name='profile'),
        path('logout/', views.user_logout, name='logout'),
        path('changepassword/', views.user_change_password, name='changepassword'),
        path('changepassword2/', views.user_change_password2, name='changepassword2'),
        path('userdetail/<int:id>', views.user_detail, name='userdetail'), 
        path('userdashboard/<int:id>', views.user_dashboard, name='userdashboard'), 
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('info/', include('info.urls')),
        path('anag/', include('anag_utenti.urls')),
        path('accounts/', include('organizations.urls')),
        path('invitations/', include(invitation_backend().get_urls())),
        path('signup/', views.user_signup, name='signup'),
        path('login/', views.user_login, name='login'),
        path('profile/', views.user_profile, name='profile'),
        path('logout/', views.user_logout, name='logout'),
        path('changepassword/', views.user_change_password, name='changepassword'),
        path('changepassword2/', views.user_change_password2, name='changepassword2'),
        path('userdetail/<int:id>', views.user_detail, name='userdetail'),
        path('userdashboard/<int:id>', views.user_dashboard, name='userdashboard'), 
    ]
#Language chooser requires 'django.middleware.locale.LocaleMiddleware' in your MIDDLEWARE to work and the following code
urlpatterns += [path(r'^i18n/', include('django.conf.urls.i18n'))]    
