from tastypie.resources import ModelResource
from question.models import *
from tastypie.authorization import Authorization
from tastypie import fields
from django.db import models

class PostResource(ModelResource):
  author = fields.CharField(attribute="author", use_in="list")
  title = fields.CharField(attribute="title", use_in="list")
  text = fields.CharField(attribute="text", use_in="list")
  is_public = fields.CharField(attribute="is_public", use_in="detail")
  comments = fields.ToManyField("question.api.CommentResource", full=True, null=True, 
      attribute=lambda bundle: Comment.objects.filter(post=bundle.obj), use_in='detail')
  class Meta:
    queryset = Post.objects.all()
    resource_name = 'post'
    authorization = Authorization()
    always_return_data = True

class CommentResource(ModelResource):
  author = fields.CharField(attribute="author", use_in="list")
  text = fields.CharField(attribute="text", use_in="list")
  post = fields.ToOneField(PostResource, 'post')
  class Meta:
    queryset = Comment.objects.all()
    resource_name = 'comment'
    authorization = Authorization()
    always_return_data = True
  
  
  
  
