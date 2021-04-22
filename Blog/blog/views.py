# from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from .models import Post
from .forms import NewUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


class BlogListView (ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView (DetailView):
    model = Post
    template_name = 'post_detail.html'


def RegisterView(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid ():
            user = form.save ()
            messages.success (request, "Registration successful.")
            return redirect ('login')
        else:
            messages.error (request, "Unsuccessful registration. Invalid information.")
    return render (request, "register.html", context={"form": form})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password  is incorrect')
    context = {}
    return render (request, "login.html", context)


@login_required
def LogoutView(request):
    logout (request)
    return redirect('login')
