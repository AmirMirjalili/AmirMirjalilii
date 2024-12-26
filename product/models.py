from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

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
    price = models.DecimalField(max_digits=20,decimal_places=2)
    description = RichTextField(default='')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = TreeForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product',
        null = True,
        blank = True
    )
    imag = models.ImageField(upload_to='product/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_discount = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=0, default=0,help_text="Enter discount percentage (e.g., 10 for 10%)")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details_view:product_details', kwargs={'slug': self.slug})

    def get_discounted_price(self):
        if self.discount_percentage > 0:
            discount_amount = (self.discount_percentage / 100) * self.price
            discounted_price = self.price - discount_amount
            return discounted_price
        return self.price

    class Meta:
        verbose_name = "pruduct"
        verbose_name_plural = "pruducts"