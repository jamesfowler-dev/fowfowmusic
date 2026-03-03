from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = [
        ('music', 'Music'),
        ('preset', 'Preset Pack'),
        ('tuition', 'Tuition'),
    ]
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    image = CloudinaryField('images')
    file = models.FileField(upload_to='product_files/', blank=True)
    soundcloud_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
