# Generated by Django 5.0.4 on 2024-05-31 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_discount_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_percentage',
        ),
    ]