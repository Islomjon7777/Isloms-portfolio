from django.shortcuts import render

def index(request):
    # ctx = {
    #     'title': 'mening sahifam',  
    # }
    return render(request, 'index.html')
