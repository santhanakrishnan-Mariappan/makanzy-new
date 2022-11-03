from datetime import datetime

from django.db import models
# from django.db.models.functions import datetime

User_CHOICES = [
        ('Business User', 'BusinessUser'),
        ('Personal User', 'Personal User'),
    ]
# Create your models heree.
class Units(models.Model):
    location = models.CharField(max_length=265)
    buildings = models.CharField(max_length=265)
    unitTypes = models.CharField(max_length=265)
    dimensions = models.CharField(max_length=265)
    priceRange = models.IntegerField()
    amenity = models.CharField(max_length=265)
    slug = models.SlugField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    userType = models.CharField(max_length=265, choices=User_CHOICES, default=User_CHOICES[0][0])

    def __str__(self):
        return (self.location + self.buildings + self.unitTypes)

