# Generated by Django 4.2 on 2024-12-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_delete_productadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
