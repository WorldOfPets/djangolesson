from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    id_published = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']