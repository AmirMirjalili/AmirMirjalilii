from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse

class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20,)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = TreeForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product'
    )
    picture = models.ImageField(upload_to='product/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_special = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details_view:product_details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "pruduct"
        verbose_name_plural = "pruducts"