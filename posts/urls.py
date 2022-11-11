from django.urls import path, include
from posts import views

app_name = "posts"


urlpatterns = [
    path('create/', views.create_post, name="create_post"),
    path('my-posts/', views.my_posts, name="my_posts")

]
