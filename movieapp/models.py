from django.db import models
from django.urls import reverse
# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    poster = models.ImageField(upload_to='Poster', blank=True)
    class Meta:
        ordering=('title',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movieapp:movie_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.title)



class Movie(models.Model):
    title = models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True)
    release_date = models.DateField(blank=True)
    poster= models.ImageField(upload_to='Gallery',blank=True)
    actor=models.CharField(max_length=100)
    actress=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    ylink=models.URLField(blank=True)
    available=models.BooleanField(default=True)
    review=models.TextField(blank=True)
    ratings= models.DecimalField(max_digits=250,decimal_places=1,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('movieapp:MovieDetail', args=[self.category.slug, self.slug])

    class Meta:
            ordering = ('title',)
            verbose_name = 'movie'
            verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.title)



