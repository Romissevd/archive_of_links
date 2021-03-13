from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib import auth


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    errors = []
    if request.method == 'POST':
        login = request.POST.get('login', '')
        passwd = request.POST.get('password', '')
        if errors:
            return render(request, 'login.html', {
                'form': LoginForm,
                'errors': errors,
                })

        user = auth.authenticate(
            username=login,
            password=passwd,
        )
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(f'{request.path}')
        else:
            errors.append('Wrong login or password.')
            return render(request, 'login.html', {
                'form': LoginForm,
                'errors': errors,
            })
    else:
        return render(request, 'login.html', {'form': LoginForm})
