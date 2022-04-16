from django.db import models
from django.urls import reverse
from datetime import date

CITIES = (
    ('SF', 'San Francisco'),
    ('LA', 'Los Angeles'),
    ('SD', 'San Diego'),
    ('NY', 'New York'),
)
class Venue(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('venues_detail', kwargs={'pk': self.id})

class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=100)
    location = models.TextField(max_length=200)
    venue = models.ManyToManyField(Venue)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'artist_id': self.id})

class Shows(models.Model):
    date = models.DateField('Next show')
    city = models.CharField(
        'choose city',
        max_length=2,
        choices = CITIES,
        default = CITIES[0][0]
    )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_city_display()} on {self.date}"

class Meta:
    ordering = ['-date']