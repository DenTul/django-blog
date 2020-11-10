from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost, BlogCategory


def index_blog_page(request):
    blog_posts = BlogPost.objects.all()
    blog_categories = BlogCategory.objects.all()
    context = {
        "blog_posts": blog_posts,
        "blog_categories": blog_categories
    }
    return render(request, "blog/index_blog_page.html", context=context)


def blog_by_category(request, pk):
    blog_posts_by_category = BlogPost.objects.filter(topic_id=pk)
    blog_categories = BlogCategory.objects.all()
    cur_category = BlogCategory.objects.get(pk=pk)

    context = {
        "blog_posts_by_category": blog_posts_by_category,
        "blog_categories": blog_categories,
        "cur_category": cur_category
    }

    return render(request, "blog/blog_posts_by_category.html", context=context)


def single_blog_page(request, pk):
    single_news = BlogPost.objects.get(pk=pk)
    blog_categories = BlogCategory.objects.all()

    context = {
        "single_news": single_news,
        "blog_categories": blog_categories
    }

    return render(request, "blog/single_blog_page.html", context=context)
