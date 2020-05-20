""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='blog_home'),
    path('<int:blog_id>',views.blog_detail,name="blog_detail")
]