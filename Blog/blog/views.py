# from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import NewUserForm, CommentForm
from .models import Post, Comment


# Create your views here.


class BlogListView (ListView):
    model = Post
    template_name = 'home.html'


# class BlogDetailView (DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     comments = Comment


def BlogDetailView (request, pk):
    post = Post.objects.get (pk=pk)

    form = CommentForm ()
    if request.method == 'POST':
        form = CommentForm (request.POST)
        if form.is_valid ():
            comment = Comment (
                author=form.cleaned_data["name"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save ()

    comments = Comment.objects.filter (post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render (request, "post_detail.html", context)


def RegisterView (request):
    form = NewUserForm ()
    if request.method == "POST":
        form = NewUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            messages.success (request, "Registration successful.")
            return redirect ('login')
        else:
            messages.error (request, "Unsuccessful registration. Invalid information.")
    return render (request, "register.html", context={"form": form})


class BlogCreateView (CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')


def LoginView (request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate (request, username=username, password=password)

        if user is not None:
            login (request, user)
            return redirect ('home')
        else:
            messages.info (request, 'Username or Password  is incorrect')
    context = {}
    return render (request, "login.html", context)


@login_required
def LogoutView (request):
    logout (request)
    return redirect ('login')


class BlogUpdateView (UpdateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    success_url= reverse_lazy('home')


class BlogDeleteView (DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy ('home')
