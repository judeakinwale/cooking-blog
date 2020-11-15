from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "blog"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.HomeListView.as_view(), name="home"),
    path("search/", views.SearchListView.as_view(), name="search"),
    path("articles/", views.ArticleListView.as_view(), name="article_list"),
    path("article/<slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("articles/<filter>/", views.FilteredArticleListView.as_view(), name="filtered_article"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/<slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("contact/", views.ContactUsView.as_view(), name="contact"),
]
