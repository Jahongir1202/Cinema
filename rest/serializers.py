from rest_framework import serializers
from .models import Movia, Video

class MoviaAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Movia
        fields = '__all__'

class MoviaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
