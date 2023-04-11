from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post, Message
from django.http import FileResponse
from django.conf import settings
import os
import geocoder
import json
import requests
from django.templatetags.static import static
# Create your views here.

def home(request):
    #model = Post.objects.all()
    messages = Message.objects.all()
   
    return render(request, 'index.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        message = Message.objects.create(content=request.POST['content'])
        message.save()
    return redirect('home')

def resume(request):
    return render(request,'resume.html')
