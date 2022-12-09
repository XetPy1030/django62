from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField("id", "id", True)
    title = models.CharField("title", "title", max_length=100)
    content = models.CharField("content", "content", max_length=300)
    url = models.CharField("url", "url", max_length=50)