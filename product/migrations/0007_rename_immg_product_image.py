# Generated by Django 4.2 on 2024-12-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_picture_product_immg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='immg',
            new_name='image',
        ),
    ]
