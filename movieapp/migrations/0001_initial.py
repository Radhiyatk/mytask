# Generated by Django 4.2.11 on 2024-04-08 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('poster', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('s_link', models.SlugField()),
                ('desc', models.TextField(blank=True)),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(blank=True, upload_to='movie')),
                ('actor', models.CharField(max_length=100)),
                ('actress', models.CharField(max_length=100)),
                ('ylink', models.URLField(blank=True)),
                ('review', models.TextField(blank=True)),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.category')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ('name',),
            },
        ),
    ]
