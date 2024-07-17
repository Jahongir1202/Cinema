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

class Serial(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subtitle = models.CharField(max_length=400)
    state = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    lenguage = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
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

class Video(models.Model):
    serial = models.ForeignKey(Serial, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"{self.serial.title} - Video"


class Multifilm(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subtitle = models.CharField(max_length=400)
    state = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

class MultifilmVideo(models.Model):
    multifilm = models.ForeignKey(Multifilm, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title