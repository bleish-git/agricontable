from django.utils.deprecation import MiddlewareMixin
from .models import Gruppo



class GruppoMiddleware(MiddlewareMixin):
    pass    
    """    
    def process_request(self, request):
        organization_id = self.get_organization_id(request)
        if organization_id:
            request.organization = Gruppo.objects.get(id=int(organization_id))
        else:
            request.organization = None


    def get_organization_id(self, request):
        from multigroup.models import GruppoUser
        
        if request.user.is_authenticated:
            us = GruppoUser.objects.filter(user_id = request.user.id).filter(gruppo_predefinito=1).first()
            # dalla sessione:
            return request.session.get('gruppo_utente',us.organization.id)
        # se l'utente non è loggato
        else:
            request.organization = None
    """