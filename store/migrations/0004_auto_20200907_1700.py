# Generated by Django 3.0.7 on 2020-09-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200907_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]