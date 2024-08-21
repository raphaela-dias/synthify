from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def chatsynthify(request):
    return render(request, 'chat-synthify.html')