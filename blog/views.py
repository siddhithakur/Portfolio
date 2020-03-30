from django.shortcuts import render,get_object_or_404
from .models import Blogs
def all_blogs(request):

    myblogs=Blogs.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':myblogs})


def detail(request,blog_id):

    blog=get_object_or_404(Blogs,pk=blog_id)
    return render(request,'blog/detail.html',{'id':blog})