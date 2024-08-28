from django.urls import path
from app.views import index, loginPage, chatsynthify, openTickets, sobre, upload_file, search_docs, search_tickets, myTickets

urlpatterns = [
        path('', index),
        path('loginPage.html', loginPage),
        path('chat-synthify.html', chatsynthify),
        path('open_tickets.html', openTickets),
        path('my_tickets.html', myTickets),
        path('sobre.html', sobre),
        path('chat-synthify.html/file_uploaded/', upload_file, name='upload_file'),
        path('chat-synthify.html/search_docs/', search_docs, name='search_docs'),
        path('chat-synthify.html/search_tickets/', search_tickets, name='search_tickets'),
        ]