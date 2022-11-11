import datetime
import json


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from posts.forms import PostForm
from posts.models import Author, Category,Post
from main.functions import paginate_instances


@login_required(login_url="/users/login/")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            if not Author.objects.filter(user=request.user).exists():
                author = Author.objects.create(
                    user=request.user, name=request.user.username)
            else:
                author = request.user.author
            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.author = author
            instance.save()

            tags_list = tags.split(",")
            for tag in tags_list:
                category, created = Category.objects.get_or_create(
                    title=tag.strip())
                instance.categories.add(category)

            response_data = {
                "title": "Successfully submitted",
                "message": "Successfully submitted",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')

    else:
        data = {
            "title": "Hello",
            "description": "Hello",
            'short_description': "Hello",
            "time_to_read": "8 min",
            'tags': "technology, Science, Development"
        }
        form = PostForm(initial=data)
        context = {
            "title": "Create a new post",
            'form': form,
        }
        return render(request, "posts/create.html", context=context)


@login_required(login_url="/users/login/")
def my_posts(request):
    posts = Post.objects.filter(author__user=request.user,is_deleted=False)
    instances = paginate_instances(request,posts,per_page=1)
    context={
        "title": "My Post",
        "instances": instances
    }
    return render(request,"posts/my-posts.html",context=context)
