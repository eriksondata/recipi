from django.db import models
from django.conf import settings

# Create your models here.

class measurements(models.Model):
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.long_name


class recipe(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    
    def __unicode__(self):
        return self.name


class ingredients(models.Model):
    for_recipe = models.ForeignKey(recipe)    
    ingredient = models.CharField(max_length = 100)
    quantity = models.FloatField("Quantity (decimal)")
    measurement = models.ForeignKey(measurements)
    comment = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s %s - %s - %s' % (self.quantity, self.measurement, self.ingredient, self.comment[:100])
    
    
class directions(models.Model):
    for_recipe = models.ForeignKey(recipe)
    step_number = models.IntegerField()
    description = models.TextField()
    
    def __unicode__(self):
        return '%s - %s' % (self.step_number, self.description[:50])