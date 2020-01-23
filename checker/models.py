from django.contrib.auth.models import User
# from django.shortcuts import reverse
from django.urls import reverse
from django.db import models

# Create your models here.


class UrlsChecker(models.Model):
    INTERVAL = (
        (3000, '3 second'),
        (5000, '5 seconds'),
        (10000, '10 seconds')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Posted by')
    links = models.ManyToManyField('Link', related_name='links')
    interval = models.IntegerField(choices=INTERVAL, default=3000)

    def get_update_url(self):
        return reverse('checker:checker_update_url', args=[self.id])

    class Meta:
        ordering = ['-pk']


class Link(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.title
