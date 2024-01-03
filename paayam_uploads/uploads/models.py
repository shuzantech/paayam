from django.db import models

# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Media(models.Model):
    image = models.ImageField(upload_to="image")
    file = models.FileField(upload_to="file")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.image)[6:]
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =  ''
        return url
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")

    def __str__(self):
        return str(self.image)[8:]
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =  ''
        return url
    
class Publications(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="publications", null=True, blank=True)
    file = models.FileField(upload_to="publications")
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url =  ''
        return url