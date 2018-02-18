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

#from pyapp import views
from pyapp.views import *
from admin.views import *

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^login_form$',views.login_form),
    # url(r'^logged_in_only$',views.logged_in_only),
    # url(r'^signup/$', views.signup),
    url(r'^allCats/$', all_categories),
    url(r'^allCats/(?P<name>[a-z]+)/$',post_by_category),
    url(r'^allPosts$', all_posts),
    url(r'^user/(?P<user_id>[0-9]+)/$',get_user),
    url(r'^posts/(?P<post_id>[0-9]+)/$',show_post),
    url(r'^comments/(?P<post_id>[0-9]+)/$',show_comments),
    url(r'^allusers/', allUsers),
    url(r'^block/(?P<usr_id>[0-9]+)/$',user_block),
    url(r'^unblock/(?P<usr_id>[0-9]+)$',user_unblock),
    url(r'^promote/(?P<usr_id>[0-9]+)$',user_promote),
    url(r'^allcategories/$', allCategories),
    url(r'^allcategories/new/$',category_new),
    url(r'^allcategories/(?P<cat_id>[0-9]+)/update',category_update),
    url(r'^allcategories/(?P<cat_id>[0-9]+)/delete', category_delete),
    url(r'^allbadwords/$', allBadwords),
    url(r'^allbadwords/new/$',badword_new),
    url(r'^allbadwords/(?P<word_id>[0-9]+)/update',badword_update),
    url(r'^allbadwords/(?P<word_id>[0-9]+)/delete', badword_delete),
]
