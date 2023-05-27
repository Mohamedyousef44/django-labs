from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid


class Isbn(models.Model):
    author_title = models.CharField(max_length=30)
    book_title = models.CharField(max_length=30)
    isbn = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.author_title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    author_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    rate = models.IntegerField()
    views = models.IntegerField()
    slug = models.SlugField(unique=True, max_length=255, blank=True , editable=False)
    user = models.ForeignKey(User , on_delete=models.PROTECT)
    isbn = models.OneToOneField(Isbn , on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.author_name
