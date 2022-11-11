from django.db import models
from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=25)
    short_description = models.TextField()
    description = RichTextField()
    time_to_read = models.CharField(max_length=128)
    featured_image = models.ImageField(upload_to="posts/")

    author = models.ForeignKey("posts.Author", on_delete=models.CASCADE)
    published_date = models.DateField()
    categories = models.ManyToManyField("posts.Category")
    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
