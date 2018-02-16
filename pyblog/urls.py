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
# from pyapp import views
from pyapp.views import all_categories,post_by_category,show_post

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^login_form$',views.login_form),
    # url(r'^logged_in_only$',views.logged_in_only),
    # url(r'^signup/$', views.signup),
    url(r'^allCats/$', all_categories),
    url(r'^allCats/(?P<name>[a-z]+)/$',post_by_category),
    url(r'^posts/(?P<post_id>[0-9]+)/$',show_post),
]
