from django.db import models



class Cinema(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subtitle = models.CharField(max_length=400)
    state = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    lenguage = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    video_file = models.FileField(upload_to='videos/')
    GENRE_CHOICES = [
        ('action', 'Jangari'),
        ('comedy', 'Komedia'),
        ('drama', 'Drama'),
        ('horror', 'Qorqinchili'),
        ('romance', 'Romance'),
        ('fantastik', 'Fantastik'),
        ('hayotiy', 'hayotiy'),
        # Boshqa janrlarni ham qo'shishingiz mumkin
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)



    def __str__(self):
        return self.title

# Create your models here.
