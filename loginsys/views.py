from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm



def login(request):
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            context['username'] = user
            return redirect("/")
        else:
            context['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect("/")
def register(request):
    context = {}
    context.update(csrf(request))
    context['form'] = UserCreationForm()
    context['username'] = auth.get_user(request).username
    if request.method == "POST":
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect("/")
        else:
            context['form'] = newuser_form
    return render(request, 'register.html', context)
