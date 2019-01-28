from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    is_active = models.BooleanField(default=True)

    def __str__(self):
            return self.title


class Comment(models.Model):
        post = models.ForeignKey(Post,
                    on_delete=models.CASCADE, related_name = "name")

        date_created = models.DateTimeField('date created')
        content = models.TextField(max_length=200)
