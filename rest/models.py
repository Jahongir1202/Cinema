from django.db import models

class Movia(models.Model):
    TYPE_CHOICES = [
        ('cinema', 'cinema'),
        ('serial', 'serial'),
        ('multifilm', 'multifilm'),
    ]
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subtitle = models.CharField(max_length=400)
    state = models.CharField(max_length=50)
    years = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=200)
    GENRE_CHOICES = [
        ('jangari', 'jangari'),
        ('komedia', 'komedia'),
        ('drama', 'drama'),
        ('ujas', 'ujas'),
        ('romance', 'romance'),
        ('fantastik', 'fantastik'),
        ('hayotiy', 'hayotiy'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

class Video(models.Model):
    movia = models.ForeignKey(Movia, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
