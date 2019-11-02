from django.shortcuts import render
from .models import Spam

# Create your views here.


def spam_list(request):
    spams = Spam.objects.all()
    return render(request, 'spam/spam_list.html', {'spams': spams})
