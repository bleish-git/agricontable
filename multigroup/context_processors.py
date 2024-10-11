def custom_context(request):
    from multigroup.models import GruppoUser, Gruppo

    session = request.session
    us = GruppoUser.objects.filter(user_id = request.user.id).filter(gruppo_predefinito=1).first()
    
    #TODO inserire nell'elif un context che nasconda il pulsante cambia, in quanto vuol dire che l'utente 
    #si sta loggando o ha fatto logout e non ha senso vederel il pulsante

    if not 'gruppo_utente' in request.session and hasattr(us,'organization_id'):
        request.session['gruppo_utente']=us.organization_id
        titolo_gruppo = Gruppo.objects.get(id=request.session['gruppo_utente']).nomeEsteso
    elif not 'gruppo_utente' in request.session:
        titolo_gruppo = ""
    else:
        titolo_gruppo = Gruppo.objects.get(id=request.session['gruppo_utente']).nomeEsteso
        

      
    return {'gruppo_utente': titolo_gruppo, 'cambia': "change", 'cambia_gruppo_link':'' }