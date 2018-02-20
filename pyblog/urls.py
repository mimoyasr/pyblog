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
    url(r'^home/$', home),
    url(r'^unsup/(?P<user_id>[0-9]+)/(?P<cat_id>[0-9]+)/', un_sup),
    url(r'^sup/(?P<user_id>[0-9]+)/(?P<cat_id>[0-9]+)/', sup),
    url(r'^allCats/(?P<name>[a-z]+)/$', post_by_category),
    url(r'^allPosts$', all_posts),
    url(r'^category/(?P<cat_id>[0-9]+)/$', get_category),
    url(r'^user/(?P<user_id>[0-9]+)/$',get_user),
    url(r'^posts/(?P<post_id>[0-9]+)/$',show_post),
    url(r'^comments/(?P<post_id>[0-9]+)/$',show_comments),
    url(r'^allusers/', allUsers),
    url(r'^block/(?P<usr_id>[0-9]+)/$',user_block),
    url(r'^unblock/(?P<usr_id>[0-9]+)$',user_unblock),
    url(r'^promote/(?P<usr_id>[0-9]+)$',user_promote),
    url(r'^(?P<usr_id>[0-9]+)/delete', user_delete),
    url(r'^allcategories/$', allCategories),
    url(r'^allcategories/new/$',category_new),
    url(r'^allcategories/(?P<cat_id>[0-9]+)/update',category_update),
    url(r'^allcategories/(?P<cat_id>[0-9]+)/delete', category_delete),
    url(r'^allbadwords/$', allBadwords),
    url(r'^allbadwords/new/$',badword_new),
    url(r'^allbadwords/(?P<word_id>[0-9]+)/update',badword_update),
    url(r'^allbadwords/(?P<word_id>[0-9]+)/delete', badword_delete),
    url(r'^allposts/',allPosts),
    url(r'^allposts/new/$',post_new),
    url(r'^post/(?P<post_id>[0-9]+)/edit',Posts_edit),
    url(r'^post/(?P<post_id>[0-9]+)/del',Post_delete),
    url(r'^index',admin),

]
