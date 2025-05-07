from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm #, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from multigroup.models import GruppoUser


def index(request):
    # Page from the theme 
    return render(request, 'dashboard/pages/index.html')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account in attesa di convalida da parte del gruppo')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'dashboard/signup.html', {'form':fm})



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                user_password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login avvenuto con successo.')
                    return HttpResponseRedirect('/home/')
        else:
            fm = LoginForm()
        return render(request, 'dashboard/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/home/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profilo aggiornato.')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'dashboard/profile.html', 
            {'name': request.user.username, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change password with old password
def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # Update user session
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password cambiata con successo.')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'dashboard/changePassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

# Change password without old password
def user_change_password2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # Update user session
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password cambiata con successo.')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'dashboard/changePassword2.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'dashboard/userdetail.html', 
            {'name': request.user.username,'form': fm})
    else:
        return HttpResponseRedirect('/login/')

def user_dashboard(request, id, idorg):
    if request.user.is_authenticated:

        user_organizations = GruppoUser.objects.filter(user=request.user).select_related('organization')
        #self.fields['organization'] = forms.ChoiceField(choices=[(o.organization_id, str(o.organization)) for o in GruppoUser.objects.filter(user=current_user)])


        return render(request, 'dashboard/userdashboard.html', 
            {'name': request.user.username, 'organizations': user_organizations, 'default_org':idorg})
    else:
        return HttpResponseRedirect('/login/')