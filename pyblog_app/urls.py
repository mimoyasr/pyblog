from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^index',views.admin),
    url(r'^navbar',views.nav),
    url(r'^tables',views.table),
    url(r'^allposts',views.allPosts),
    url(r'^post/new',views.post_new),
]
