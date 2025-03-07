from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ""
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:

                if user.poste == 'medecin_chef_de_zone':
                    login(request,user)
                    return redirect('/')

                else:
                    msg = 'Poste invalide'
            else:
                msg = 'Email ou mot de passe invalide'
        else:
            msg = 'Erreur de validation'
    return render(request, 'login.html', {'form': form, 'msg': msg })


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.poste == 'ministre_national':
                msg = 'Vous n\'êtes pas autorisé à enregistrer un deuxième ministre national'
            else:
                user.save()
                msg = 'Utilisateur créé'
                return redirect('/')
        else:
            msg = 'Informations invalides'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')