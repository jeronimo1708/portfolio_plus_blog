from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("posts", all_blogs, name="all_blogs_view"),
    path("posts/<slug:slug>", single_blog, name="selected_blog_view"), # this slug is replaced by dynamic blog entry
]