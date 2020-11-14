from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, View
from .forms import ContactUsForm
from .models import Article, Category

# Create your views here.


class SearchListView(ListView):
    paginate_by = 15
    template_name = "blog/article_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        try:
            object_list = Article.objects.filter(Q(title__icontains=query))
            return object_list
        except:
            null_search = "We can't find that article"
            return null_search
        

def search(request):

    pass
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context


class HomeListView(ListView):
    model = Article
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        queryset = Article.objects.order_by("-timestamp")
        queryset_popular = Article.objects.order_by("-view_count")
        queryset_editors_pick = queryset.filter(is_editors_pick=True)
        queryset_is_trending = queryset.filter(is_trending=True)
        cat_query = Category.objects.all()
        featured_cat_query = cat_query.filter(is_featured=True)
        featured_editors_pick_query = queryset.filter(is_featured=True, is_editors_pick=True)

        
        featured_cat_1 = featured_cat_query[0]
        featured_cat_2 = featured_cat_query[1]
        trending_category_1 = queryset.filter(category=featured_cat_1)
        trending_category_2 = queryset.filter(category=featured_cat_2)
        

        context = super().get_context_data(**kwargs)
        context["recent_articles"] = queryset[:4]
        context["popular_articles"] = queryset_popular[:4]
        context["categories"] = cat_query

        context["editors_pick_1"] = queryset_editors_pick[0]
        context["editors_picks"] = queryset_editors_pick[1:4]
        context["trending_articles"] = queryset_is_trending[:4]


        context["featured_category_1"] = featured_cat_1.name
        context["featured_category_2"] = featured_cat_2.name
        context["featured_category_article_1"] = trending_category_1[:3]
        context["featured_category_article_2"] = trending_category_2[:3]
        
    
        context["featured_editors_pick_1"] = featured_editors_pick_query[0]
        context["featured_editors_pick_2"] = featured_editors_pick_query[1]
        context["featured_editors_pick_3"] = featured_editors_pick_query[2]
        
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 6
    template_name = "blog/article_list.html"

    def get_context_data(self, **kwargs):
        queryset = Article.objects.order_by("-timestamp")
        queryset_popular = Article.objects.order_by("-view_count")
        cat_query = Category.objects.all()
        
        context = super().get_context_data(**kwargs)
        context["popular_articles"] = queryset_popular[:4]
        context["categories"] = cat_query
        
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"   

    def get_context_data(self, **kwargs):
        queryset = Article.objects.order_by("-timestamp")
        queryset_popular = Article.objects.order_by("-view_count")
        cat_query = Category.objects.all()
        
        context = super().get_context_data(**kwargs)
        context["popular_articles"] = queryset_popular[:4]
        context["categories"] = cat_query
        
        return context


class CategoryListView(ListView):
    model = Category
    paginate_by = 20
    template_name = "blog/category_list.html"

    def get_context_data(self, **kwargs):
        queryset = Article.objects.order_by("-timestamp")
        queryset_popular = Article.objects.order_by("-view_count")
        cat_query = Category.objects.all()
        
        context = super().get_context_data(**kwargs)
        context["popular_articles"] = queryset_popular[:4]
        context["categories"] = cat_query
        
        return context


class CategoryDetailView(TemplateView):
    # model = Category
    # paginate_by = 9
    template_name = "blog/category_detail.html"

    def get_context_data(self, *args, **kwargs):
        slugged_category = Category.objects.all().filter(slug=kwargs['slug'])[0]
        queryset_by_category = Article.objects.order_by("-timestamp").filter(category=slugged_category)
        
        paginator = Paginator(queryset_by_category, 9)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        queryset_popular = Article.objects.order_by("-view_count")
        cat_query = Category.objects.all()
        
        context = super().get_context_data(**kwargs)
        context["popular_articles"] = queryset_popular[:4]
        context["categories"] = cat_query
        context["page_obj"] = page_obj
        context["slugged_category"] = slugged_category
        
        return context


# class CategoryDetailView(View):

#     def get(self, *args, **kwargs):
#         # queryset_by_category = Article.objects.order_by("-timestamp").filter(category__icontains=kwargs)
#         qq = Article.category
#         print(qq)
#         queryset_by_category = Article.objects.order_by("-timestamp").filter(category=kwargs)
#         queryset_popular = Article.objects.order_by("-view_count")
#         cat_query = Category.objects.all()
#         return render(self.request, 'blog/category_detail.html', {'category_queryset': queryset_by_category})

# def category_detail(request, slug):
#     category.objects.all().filter(slug=slug)


class ContactUsView(View):

    def get(self, *args, **kwargs):
        form = ContactUsForm()
        template_name = "blog/contact.html"
        context = {"form": form}
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        form = ContactUsForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
        return redirect("blog:contact")


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ContactUsForm()
#     return render(request, 'name.html', {'form': form})
