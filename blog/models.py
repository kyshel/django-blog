from __future__ import unicode_literals

from django.db import models


# Create your models here.



class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.TextField()
    post_date = models.DateTimeField('date published')
    post_author = models.CharField(max_length=50)

    def __str__(self):
        return self.post_title


