from django.db import models
# Create your models here.


class URL(models.Model):
    url = models.TextField()
    short_url = models.TextField(unique=True)

    def save(self, *args, **kwargs):
        self.short_url = f'localhost:8000/url-{self.id}'
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
