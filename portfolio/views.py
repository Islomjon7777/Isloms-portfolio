from django.shortcuts import render, redirect
from .models import PostModel, PortfolioModel
from .forms import ContactForm
from django.http import HttpResponse
from telegram import Bot
from datetime import datetime
import requests

def index(request):
    return render(request, 'index.html',)

def HomeView(request):
    
    return render(request, 'home.html') 
    
def AboutView(request):

    return render(request, 'about.html')


def BlogView(request):
    posts = PostModel.objects.all()

    ctx = {
        'posts': posts,
    }

    return render(request, 'blog.html', ctx)


def PortfolioView(request):
    portfolio = PortfolioModel.objects.all()

    ctx = {
        'portfolio': portfolio
    }

    return render(request, 'portfolio.html', ctx)


def ContactView(request):
    
    
    return render(request, 'contact.html',)
    



def success_view(request):
    return render(request, 'success.html')