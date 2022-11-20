from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    
class Categories(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL' )

    def get_absolute_url(self):
        return reverse('category', kwargs={'cats_id':self.slug})

    def __str__(self) -> str:
        return self.title
class News(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    id_published = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
     
    def get_absolute_url(self):
        return reverse('newsid', kwargs={'news_id':self.slug})
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    