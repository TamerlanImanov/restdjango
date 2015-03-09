from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	author  = models.CharField(max_length=100)
	tittle = models.CharField(max_length=100)
	text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField(default=timezone.now)
	upd_date = models.DateTimeField(default=timezone.now)
	is_public = models.BooleanField(default=False)

class Comment(models.Model):
	author = models.CharField(max_length=100)
	text = models.CharField(max_length=1000)
	pub_date = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post)
