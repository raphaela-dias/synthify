from django.urls import path
from app.views import index, loginPage, chatsynthify

urlpatterns = [
        path('', index),
        path('loginPage.html', loginPage),
        path('chat-synthify.html', chatsynthify),
]