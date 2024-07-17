# from django.contrib.auth.models import
from django.core.serializers import serialize
from rest_framework import serializers
from . import models
from .models import Cinema, Serial, Multifilm, Video, MultifilmVideo


class CinemaSerializer(serializers.Serializer):
    class Meta:
        model = Cinema
        fields = '__all__'
class SerialSerializer(serializers.Serializer):
    class Meta:
        model = Serial
        fields = ('title','photo','subtitle','state','years','lenguage','time','video_file','GENRE_CHOICES')

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = ('serial','video_file')

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = MultifilmVideo
        fields = ('multifilm','video_file')

class MultikSerializer(serializers.Serializer):
    class Meta:
        model = Multifilm
        fields = ('title','photo','subtitle','state','years','lenguage','time','video_file','GENRE_CHOICES')
