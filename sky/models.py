from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ("Breaking", "Breaking"),
    ("Entertainment", "Entertainment"),
    ("Politics", "Politics"),
    ("Business", "Business"),
    ("Health", "Health"),
)


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="images")
    other_image = models.ImageField(upload_to="other_images", blank=True, null=True)
    date_posted = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title
    
class Category(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images")
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self) -> str:
        return self.title
    

class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

