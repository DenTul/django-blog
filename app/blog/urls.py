from django.urls import path
from .views import index_blog_page, blog_by_category, single_blog_page

urlpatterns = [
    path("category/<int:pk>", blog_by_category, name="blog_by_category"),
    path("blog/<int:pk>", single_blog_page, name="single_blog_page"),
    path("", index_blog_page, name="index_blog_page")
]