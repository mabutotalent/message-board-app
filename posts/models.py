from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name_plural = 'posts'
