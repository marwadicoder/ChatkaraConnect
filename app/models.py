from django.db import models

class Caterer(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='caterers/')

    def __str__(self):
        return self.name
