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
    path("about/", TemplateView.as_view(template_name="blog/about.html"), name="about"),
    path("contact/", views.ContactUsView.as_view(), name="contact"),
]
