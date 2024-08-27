from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts", AllBlogsListView.as_view(), name="all_blogs_view"),
    path("posts/<slug:slug>", SingleBlogView.as_view(), name="selected_blog_view"), # this slug is replaced by dynamic blog entry
]