from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, View
from .forms import ContactUsForm
from .models import Article, Category

# Create your views here.


# def index(request):
#     return render(request, "blog/index.html")

class SearchListView(ListView):
    paginate_by = 15
    template_name = "blog/article_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Article.objects.filter(Q(title__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context


class HomeListView(ListView):
    model = Article
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        queryset = Article.objects.order_by("-timestamp").filter(is_editors_pick=True)
        context = super().get_context_data(**kwargs)
        context["editors_pick_1"] = queryset
        context["editors_picks"] = queryset[2:4]
        return context


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"


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
