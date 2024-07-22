from django.core.serializers import serialize
from rest_framework import serializers
from .models import Movia, Video, Comments


class MoviaAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Movia
        fields = '__all__'


class MoviaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
