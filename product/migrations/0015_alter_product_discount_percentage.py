# Generated by Django 4.2 on 2024-12-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=0, default=0, help_text='Enter discount percentage (e.g., 10 for 10%)', max_digits=5),
        ),
    ]
