from django.db import models
from django.db.models import ForeignKey


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
    views_count = models.PositiveIntegerField(default=0)  # Ko'rishlar soni
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def increment_views(self):
        self.views_count += 1
        self.save()
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




class Comments(models.Model):
    comments_id = models.ForeignKey(Movia,related_name='comments',on_delete=models.CASCADE)
    commenter = models.TextField(max_length=50)
    comments = models.TextField()

    def __str__(self):
        return f'Comment by {self.commenter} on {self.movia.title}'