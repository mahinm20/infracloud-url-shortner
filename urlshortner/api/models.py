from hashlib import new
from django.db import models
from random import choice, choices
from string import ascii_letters
from django.conf import settings

# Create your models here.
class Link(models.Model):
    original_url = models.URLField()
    short_url=models.URLField(blank=True,null=True)

    def shortenerURL(self):
        STRING_PARAMTER = ascii_letters + "1234567890"
        while True:
            str1="".join(choices(STRING_PARAMTER,k=8))

            new_url = settings.HOST_URL +"/"+str1
            if not Link.objects.filter(short_url=new_url).exists():
                break

        return new_url

    def save(self,*args, **kwargs):
        if not self.short_url:
            new_url=self.shortenerURL()
            self.short_url=new_url
        return super().save(*args, **kwargs)            
