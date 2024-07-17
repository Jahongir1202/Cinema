from rest_framework.generics import ListAPIView, RetrieveAPIView
from page.models import Cinema, Serial, Video, Multifilm, MultifilmVideo
from .serializers import CinemaSerializer, SerialSerializer, VideoSerializer, MultifilmSerializer, MultifilmVideoSerializer

class CinemaListView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaDetailView(RetrieveAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class SerialListView(ListAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer

class SerialDetailView(RetrieveAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer

class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class MultifilmListView(ListAPIView):
    queryset = Multifilm.objects.all()
    serializer_class = MultifilmSerializer

class MultifilmDetailView(RetrieveAPIView):
    queryset = Multifilm.objects.all()
    serializer_class = MultifilmSerializer

class MultifilmVideoListView(ListAPIView):
    queryset = MultifilmVideo.objects.all()
    serializer_class = MultifilmVideoSerializer

class MultifilmVideoDetailView(RetrieveAPIView):
    queryset = MultifilmVideo.objects.all()
    serializer_class = MultifilmVideoSerializer
from django.shortcuts import render

# Create your views here.
