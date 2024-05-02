from django.db import models
from django.urls import reverse
# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    poster = models.ImageField(upload_to='category', blank=True)
    class Meta:
        ordering=('title',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movieapp:movie_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.title)



class Movie(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField()
    desc = models.TextField(blank=True)
    release_date = models.DateField()
    poster= models.ImageField(upload_to='movie',blank=True)
    actor=models.CharField(max_length=100)
    actress=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    ylink=models.URLField(blank=True)
    review=models.TextField(blank=True)
    ratings= models.DecimalField(max_digits=250,decimal_places=1)


    def get_url(self):
        return reverse('movieapp:MovieDetail', args=[self.category.slug, self.slug])

    class Meta:
            ordering = ('name',)
            verbose_name = 'movie'
            verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.name)



