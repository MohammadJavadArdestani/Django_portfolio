from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs= Blog.objects
    return render(request,'blog\home.html',{'blogs':blogs})

def blog_detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog\\blogDetail.html',{'blog': blog_detail})
