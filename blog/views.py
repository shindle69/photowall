from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html',{
        'post_list':post_list,
    })
    
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{
        'post':post,
    })

def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/post_main.html',{
        'post_list':post_list,
    })