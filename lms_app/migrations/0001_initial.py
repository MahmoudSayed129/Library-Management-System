# Generated by Django 4.0.2 on 2022-02-19 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('book_img', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('auth_img', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rent_price_per_day', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rent_days', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.catagory')),
            ],
        ),
    ]