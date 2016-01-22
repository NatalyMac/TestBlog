from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, login, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', inclde('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'^comments/', include('threadedcomments.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace ='social')),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page' : '/'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view (url='/'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
    #url(r'^users/(?P<pk>\d+)/$', RedirectView.as_view(url='/'), name='register_complete'), check exp
    url(r'^accounts/profile/$', RedirectView.as_view (url='/'), name='auth_login'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    
    )
