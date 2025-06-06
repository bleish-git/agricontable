from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    from multigroup.models import GruppoUser

    session = request.session
    us = GruppoUser.objects.filter(user_id = request.user.id).filter(gruppo_predefinito=1).first()

    if ('utente' not in session or 'gruppo_utente' not in session) and us is not None:
        session['utente'] = request.user.id
        session['gruppo_utente']= us.organization.id
        request.session.save()
        messages.success(request, 'Login utente e accesso al gruppo: '+str(session.get('gruppo_utente',0))+' - '+us.organization.nomeEsteso)
    
    # TODO caso in cui il gruppo predefinito non è stato definito e quindi non conosciamo dati sul gruppo in generale
    # sarebbe utile che in fase di registrazione dell'utente, si definisca il gruppo il gruppo predefinito 
    # oppure nel caso di primo login    
    elif ('utente' not in session or 'gruppo_utente' not in session) and us is None:
        pass

    

