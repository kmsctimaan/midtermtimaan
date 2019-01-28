from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Comment
from datetime import datetime

# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'index.html', context)

def detail(request):
    context = {}
    context['posts'] = posts
    return render(request, 'detail.html', context)

def create(request):
    context = {}

    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            render(request, 'create.html', context)
    else:
        context['form'] = QuestionModelForm(initial={"pub_date": str(datetime.now())})
        return render(request, 'create.html', context)

def update(request):
    if request.method == "POST":
        posts = Post.objects.all()
        form = PostModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save
        return HttpResponse('Post Updated!')
    else:
        context['form'] = forms
        render(request, 'update.html', context)

# def comment(request):
