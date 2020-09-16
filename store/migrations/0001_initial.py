# Generated by Django 3.0.7 on 2020-09-05 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('manager', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('enugu', 'enugu')], max_length=100)),
                ('sides', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product')),
                ('desc', models.CharField(max_length=200, null=True)),
                ('time', models.IntegerField(blank=True, default='10')),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('toppings', models.BooleanField(blank=True, default=False, null=True)),
                ('available', models.BooleanField(default=True)),
                ('popular', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('class_top', models.CharField(blank=True, choices=[('price1', 'price1'), ('price2', 'price2'), ('price3', 'price3'), ('price4', 'price4'), ('price5', 'price5'), ('price6', 'price6'), ('price7', 'price7'), ('price8', 'price8')], max_length=20)),
                ('class_bottom', models.CharField(blank=True, choices=[('price', 'price'), ('price22', 'price22'), ('price33', 'price33'), ('price44', 'price44'), ('price55', 'price55'), ('price66', 'price66'), ('price77', 'price77'), ('price88', 'price88')], max_length=20)),
                ('class_btn', models.CharField(blank=True, choices=[('btn1', 'btn1'), ('btn2', 'btn2'), ('btn3', 'btn3'), ('btn4', 'btn4'), ('btn5', 'btn5'), ('btn6', 'btn6'), ('btn7', 'btn7'), ('btn8', 'btn8')], max_length=20)),
                ('slides', models.CharField(blank=True, choices=[('slider1', 'slider1'), ('slider2', 'slider2'), ('slider3', 'slider3'), ('slider4', 'slider4'), ('slider5', 'slider5'), ('slider6', 'slider6'), ('slider7', 'slider7'), ('slider8', 'slider8'), ('slider8', 'sli ')], max_length=20)),
                ('color', models.CharField(blank=True, choices=[('#E32435', '#E32435'), ('#6CD96A', '#6CD96A'), ('#4795D1', '#4795D1'), ('#292a2f', '#292a2f')], max_length=20)),
                ('color2', models.CharField(blank=True, choices=[('#A30F22', '#A30F22'), ('#00986F', '#00986F'), ('#006EB8', '#006EB8'), ('#131519', '#131519')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('auth', models.BooleanField(default=False)),
                ('manager', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('detail', models.CharField(max_length=1000)),
                ('agent', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('total', models.CharField(max_length=20, null=True)),
                ('price_check', models.BooleanField(default=False)),
                ('deliveryfee', models.IntegerField(default=0, null=True)),
                ('code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10, null=True)),
                ('side', models.CharField(max_length=50, null=True)),
                ('Net_total', models.CharField(max_length=20, null=True)),
                ('is_user', models.BooleanField(default=False)),
                ('info', models.CharField(max_length=400, null=True)),
                ('report', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Ordered', 'Ordered'), ('Cancelled', 'Cancelled'), ('Complete', 'Complete')], max_length=20)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('rate', models.FloatField(default=1)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]