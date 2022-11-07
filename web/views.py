from django.shortcuts import render 
from django.http.response import HttpResponse
from django.core import paginator, PageNotAnInteger, EmptyPage

from posts.models import Post

def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)


    
    instances = paginator(posts, 9)
    page = request.Get.get('page', 1)

    try:
        instances = instances.page(page)
    except PageNotAnInteger:    
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)    

        
    context = {
        "title" : "Home Page",
        "posts" : posts
    }
    return render(request, 'web/index.html',context=context)
