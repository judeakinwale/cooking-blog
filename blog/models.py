from django.db import models
from django.shortcuts import redirect, reverse

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to="image/%y/%m/%d/", height_field="height_field", width_field="width_field", blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField("Tag", blank=True)
    view_count= models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_published = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)
    is_editors_pick = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})

    def get_read_time(self):
        """
        Get the estimated read time of an article
        """
        pass


class Author(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField()
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to="image/%y/%m/%d/", blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:author_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category_detail", kwargs={"slug": self.slug})


class Tag(models.Model):
    """
    Tags that have a many to many field relationship to article
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150, null=True)
    message = models.TextField()
    
    def __str__(self):
        identity = f"{self.first_name} {self.last_name} : {self.email}"
        return identity
    