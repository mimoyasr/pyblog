"""pyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
#from pyapp import views
from pyapp.views import *
# from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import logout


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^login_form$',views.login_form),
    # url(r'^logged_in_only$',views.logged_in_only),
    # url(r'^signup/$', views.signup),
    url(r'^allCats/$', all_categories),
    url(r'^home/$', home),
    url(r'^unsup/(?P<user_id>[0-9]+)/(?P<cat_id>[0-9]+)/', un_sup),
    url(r'^sup/(?P<user_id>[0-9]+)/(?P<cat_id>[0-9]+)/', sup),
    url(r'^allCats/(?P<name>[a-z]+)/$', post_by_category),
    url(r'^allPosts$', all_posts),
    url(r'^category/(?P<cat_id>[0-9]+)/$', get_category),
    url(r'^user/(?P<user_id>[0-9]+)/$',get_user),
    url(r'^posts/(?P<post_id>[0-9]+)/$',show_post),
    url(r'^comments/(?P<post_id>[0-9]+)/$',show_comments),
    url(r'^base/$', base_dir),
    url(r'^home/$', home),
    url(r'^signup/$', signup),
    url(r'^login/$', login_form),
    # url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # url(r'^logout/$','django.contrib.auth.views.logout',name='logout',kwargs={'next_page': '/'}),    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'), 
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^logout/$', logout, {'next_page':settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^addcomment/(?P<text>[a-zA-Z0-9_ ]+)/(?P<post>[0-9]+)/$',add_comment),
    url(r'^allCats/(?P<name>[a-z]+)/$',post_by_category),
    url(r'^posts/(?P<post_id>[0-9]+)/$', show_post),
    url(r'^reply/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)/$',show_reply),
    url(r'^addreply/(?P<text>[a-zA-Z0-9_ ]+)/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)$',add_reply),

]
