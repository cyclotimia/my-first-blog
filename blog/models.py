from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    def author(self):
        return self.author

    def pub_date(self):
        return self.pub_date

    def publish(self):
        self.published_date = timezone.now()
        self.save()