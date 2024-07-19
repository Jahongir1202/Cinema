from rest_framework import serializers
from page.models import Cinema, Serial, Multifilm, Video, MultifilmVideo

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class MultifilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multifilm
        fields = '__all__'

class MultifilmVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultifilmVideo
        fields = '__all__'
