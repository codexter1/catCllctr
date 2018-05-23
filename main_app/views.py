from django.shortcuts import render
from .models import Cat
from .forms import CatForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import CatForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})


def post_cat(request):
	form = CatForm(request.POST)
	if form.is_valid():
		cat = form.save(commit = False)
		cat.user = request.user
		cat.save()
	return HttpResponseRedirect('/')

def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats':cats, 'form':form})

def show(request, cat_id):
	cat = Cat.objects.get(id=cat_id)
	return render(request, 'show.html', {'cat': cat})



cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]
