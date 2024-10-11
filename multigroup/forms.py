from .models import GruppoUser
from django import forms


from bootstrap_modal_forms.forms import BSModalModelForm

class BookModelForm(BSModalModelForm):
    
    def __init__(self, *args, **kwargs):    
        if 'current_user' in kwargs:
            current_user=kwargs.pop('current_user', None)
            super(BookModelForm, self).__init__(*args, **kwargs)
            #self.fields['organization'].queryset = self.fields['organization'].queryset.filter(user_id=current_user)
            self.fields['organization'] = forms.ChoiceField(choices=[(o.organization_id, str(o.organization)) for o in GruppoUser.objects.filter(user=current_user)])
        else:
            super(BookModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = GruppoUser
        fields = ['organization']
     