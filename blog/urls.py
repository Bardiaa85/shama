from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('',views.blog,name='blog'),
    # path("<slug:slug>",views. Single_blog, name="single_blog_view")
]