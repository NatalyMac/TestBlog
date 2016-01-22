from django.conf.urls import patterns, url, include
from . import views
from views import PostListView, PostDetailView, PostCreateView, PostForm
#from views import *

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    url(r'^post/new/$', PostCreateView.as_view(), kwargs={'next_page' : 'home'}, name='post_new'),
    url(r'^social/', include('social.apps.django_app.urls', namespace ='social')),
    #url(r'^blog/new/$', views.post_new, name='post_new') 
    #url(r'^social/', include('social.apps.django_app.urls', namespace ='social')),
   

)
