from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import BookModelForm
from .models import GruppoUser
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib import messages

#dopo aver cambiato il gruppo_utente si porta nella pagina admin
def cambia_gruppo2(request):
    context = {"latest_question_list": 'ciccio'}
    #return render(request, 'admin/popup.html', context)
    return redirect('/admin/')

#ricarica la stessa pagina dopo aver cambiato il gruppo_utente
def cambia_gruppo(request):
    from django.http import HttpResponseRedirect

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cambia_gruppo_modal(request):
    template_name = 'admin/modal.html'
    form_class = BookModelForm(current_user=request.user.id)
    #success_message = 'Ok. Gruppo Cambiato'
    #success_url = reverse_lazy('index')
    nomecomp = User.objects.filter(id=request.user.id).get().last_name + ' ' + User.objects.filter(id=request.user.id).get().first_name
    return render(request, 'admin/modal.html', {'user':nomecomp, 'form':form_class})

def set_gruppo(request):
    from django.http import HttpResponseRedirect
    
    #success_message = 'Success: Sign up succeeded. You can now Log in.'
    #success_url = reverse_lazy('admin')
    if request.method == "POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            txt = request.POST.get('organization')
            request.session['gruppo_utente']=int(txt)
            request.session.save()
            messages.success(request, 'Operazione eseguita con successo! ' )
            
        else:
            messages.error(request, 'Operazione non andata a buon fine! ')

    return redirect('/admin/')
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
