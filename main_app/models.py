from django.db import models
from django.urls import reverse

CITIES = (
    ('SF', 'San Francisco'),
    ('LA', 'Los Angeles'),
    ('SD', 'San Diego'),
    ('NY', 'New York'),
)
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=100)
    location = models.TextField(max_length=200)
        
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

    