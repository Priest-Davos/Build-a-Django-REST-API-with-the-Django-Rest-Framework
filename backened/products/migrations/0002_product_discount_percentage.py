# Generated by Django 5.0.4 on 2024-05-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]