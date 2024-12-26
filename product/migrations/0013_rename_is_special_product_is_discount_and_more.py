# Generated by Django 4.2 on 2024-12-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_special',
            new_name='is_discount',
        ),
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Enter discount percentage (e.g., 10 for 10%)', max_digits=5),
        ),
    ]
