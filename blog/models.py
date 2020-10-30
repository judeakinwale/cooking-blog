from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to="media", height_field="height_field", width_field="width_field", blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)    
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_published = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)
    is_editors_pick = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class Author(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField()
    # slug = models.SlugField(unique=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
