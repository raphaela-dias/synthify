from django.urls import path
from app.views import index, loginPage

urlpatterns = [
        path('', index),
        path('loginPage.html', loginPage)
]