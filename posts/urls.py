from django.urls import path, include
from posts import views

app_name = "posts"


urlpatterns = [
    path('create', views.create_post, name="create_post")

]
