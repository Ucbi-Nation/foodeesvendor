# Generated by Django 3.0.7 on 2020-09-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('yoghurt', 'yoghurt'), ('shawarma', 'shawarma'), ('cake', 'cake'), ('pop-corn', 'pop-corn'), ('smothie', 'smothie'), ('grill', 'grill'), ('bread', 'bread')], max_length=20),
        ),
    ]
