from django.conf.urls import patterns, include, url
from django.contrib import admin

from question.api import *

post_res = PostResource()
comment_res = CommentResource()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'rest_project.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^api/v1/', include(post_res.urls)),
  url(r'^api/v1/', include(comment_res.urls)),
)