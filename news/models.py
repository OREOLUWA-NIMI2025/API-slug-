from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify



class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    image = models.ImageField(default="image.png", blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='News'
    
