# Generated by Django 4.2 on 2024-12-19 04:54

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_image_product_pictur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category'),
        ),
    ]