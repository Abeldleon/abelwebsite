from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Post
# Create your views here.
def chat(request):
    model = Post.objects.all()
    return render(request, 'index.html', {'posts': model})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
        return redirect('blog_post_list')
    else:
        return render(request, '/create_post.html')