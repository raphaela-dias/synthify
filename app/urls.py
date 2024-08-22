from django.urls import path
from app.views import index, loginPage, chatsynthify, openTickets, sobre, upload_file

urlpatterns = [
        path('', index),
        path('loginPage.html', loginPage),
        path('chat-synthify.html', chatsynthify),
        path('open_tickets.html', openTickets),
        path('sobre.html', sobre),
        path('chat-synthify.html/file_uploaded/', upload_file, name='upload_file'),
        ]