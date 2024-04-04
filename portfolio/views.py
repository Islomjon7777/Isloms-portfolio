from django.shortcuts import render, redirect
from .models import PostModel
from .forms import ContactForm
from telegram import Bot

def index(request):
    posts = PostModel.objects.all()

    # telegram bot messege bot
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            bot_token = '7193997385:AAEatYw-MY2ubw8reQX-gBfw6TecfP6hjk4'
            bot = Bot(token=bot_token)
            bot.send_message(text=f'Name: {name}\nEmail: {email}\n\n{message}')
            print(name)
            print(email)
            print(message)
            return redirect('success/')
        else:
            return redirect('/')
    else:
        form = ContactForm()

    
    ctx = {
        'posts': posts,
        'form': form
    }
    return render(request, 'index.html', ctx)



def success_view(request):

    return render(request, 'success.html')