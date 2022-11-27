from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name
        
class News(models.Model):
    titel = models.CharField(max_length=150, blank=False)
    content = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_publised = models.BooleanField(default=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titel

