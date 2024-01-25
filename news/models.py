from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.TextField() 

    def __str__(self):
        return self.name    


class Text(models.Model):
    full_text=models.TextField()
    text= models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

