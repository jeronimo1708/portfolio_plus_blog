from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post


def home(request):
    '''
        This function renders the home page of
        www.jeronimodcosta.com
    '''
    return render(
        request, 'my_blog/home.html'
    )

def all_blogs(request):
    '''
        This function renders all the blogs of the site
    '''
    posts = Post.objects.all().order_by("-date_updated")
    return render(
        request, 'my_blog/all_blogs.html',
        {
            "blogs" : posts,
        }
    )

def single_blog(request, slug):
    '''
        This function renders the single blog of the site
    '''
    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request, 'my_blog/blog_view.html',
        {
            "blog" : identified_post,
        }
    )
