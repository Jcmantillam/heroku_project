from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'init/index.html')

def gallery(request):
    return render(request,'init/gallery.html')

def game(request):
    return render(request,'init/game.html')

