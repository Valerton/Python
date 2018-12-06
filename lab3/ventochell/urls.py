from django.urls import path,re_path, include  
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.start, name="start"),
    path('myevents',views.myevents, name="myevents"),
    path('createEvent',views.createEvent, name="createEvent"),
    path('profile',views.profile, name="profile"),
    path('register',views.register, name="register"),
    path('index',views.index, name="index"),
    path('add',views.add,name="add"),
    re_path(r'^edit/(?P<id>\d+)$', views.edit,name="edit"),
    re_path(r'^editprofile/(?P<id>\d+)$', views.editprofile,name="editprofile"),
    re_path(r'^updateprofile/(?P<id>\d+)$', views.updateprofile,name="updateprofile"),
    re_path(r'^update/(?P<id>\d+)$', views.update,name="update"),
    re_path(r'^delete/(?P<id>\d+)$', views.destroy,name="delete")
]
