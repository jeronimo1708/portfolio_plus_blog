from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from .models import Post
from .forms import CommentForm


class HomeView(TemplateView):
    template_name = 'my_blog/home.html'

# def home(request):
#     '''
#         This function renders the home page of
#         www.jeronimodcosta.com
#     '''
#     return render(
#         request, 'my_blog/home.html'
#     )

class AllBlogsListView(ListView):
    '''
        This function renders all the blogs of the site
    '''
    # List view
    # Good for fetching data from a model
    template_name = 'my_blog/all_blogs.html'
    model = Post
    ordering = ["-date_updated"]
    context_object_name = "blogs"

    # to adjust the query logic
    # def get_queryset(self):
    #     query = super().get_queryset()
    #     data = query.order_by("-date_updated")
    #     return data
    

    # Template based class view

    # template_name = 'my_blog/all_blogs.html'

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     posts = Post.objects.all().order_by("-date_updated")
    #     context["blogs"] = posts
    #     return context
    
    

    # def get(self, request):
    #     posts = Post.objects.all().order_by("-date_updated")
    #     return render(
    #         request, 'my_blog/all_blogs.html',
    #         {
    #             "blogs" : posts,
    #         }
    #     )

# Function view

# def all_blogs(request):
#     '''
#         This function renders all the blogs of the site
#     '''
#     posts = Post.objects.all().order_by("-date_updated")
#     return render(
#         request, 'my_blog/all_blogs.html',
#         {
#             "blogs" : posts,
#         }
#     )

class SingleBlogView(View):
    # TODO: Add Tags and File uploads to the Blog
    # Detail View

    # Because we want both post and get requests in this
    # We can using the defailt view method
    # template_name = 'my_blog/blog_view.html'
    # model = Post
    # context_object_name = "blog"

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        identified_post = get_object_or_404(Post, slug=slug)
        return render(
            request, 'my_blog/blog_view.html',
            {
                "blog" : identified_post,
                "comment_form" : CommentForm()
            }
        )


    def post():
        pass

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     return context

    # Template View

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     identified_post = get_object_or_404(Post, slug=kwargs["slug"])
    #     context["blog"] = identified_post
    #     return context

# def single_blog(request, slug):
#     '''
#         This function renders the single blog of the site
#     '''
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(
#         request, 'my_blog/blog_view.html',
#         {
#             "blog" : identified_post,
#         }
#     )

class WriteBlogView(CreateView):
    # For create view - saves to db is made by default by giving the Post model
    model = Post    
    form_class = None
    template_name = None
    success_url = None
    # Form View
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    

