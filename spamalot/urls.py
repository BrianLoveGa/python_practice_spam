from django.urls import path
from . import views

urlpatterns = [
    path('', views.spam_list, name='spam_list'),
]