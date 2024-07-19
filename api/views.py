from rest_framework.generics import ListAPIView, RetrieveAPIView,GenericAPIView
from page.models import Cinema, Serial, Video, Multifilm, MultifilmVideo
from .serializers import CinemaSerializer, SerialSerializer, VideoSerializer, MultifilmSerializer, MultifilmVideoSerializer
from rest_framework.response import Response


class AllModelsListView(GenericAPIView):
    queryset = Cinema.objects.all()  # Bu faqat ruxsat berish klassi uchun kerak
    serializer_class = CinemaSerializer  # Bu ham faqat ruxsat berish klassi uchun kerak

    def get(self, request):
        cinemas = Cinema.objects.all()
        serials = Serial.objects.all()
        videos = Video.objects.all()
        multifilms = Multifilm.objects.all()
        multifilm_videos = MultifilmVideo.objects.all()

        cinema_serializer = CinemaSerializer(cinemas, many=True)
        serial_serializer = SerialSerializer(serials, many=True)
        multifilm_serializer = MultifilmSerializer(multifilms, many=True)
        return Response({
            'cinemas': cinema_serializer.data,
            'serials': serial_serializer.data,
            'multifilms': multifilm_serializer.data,
        })

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

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serial_serializer = self.get_serializer(instance)
        videos = instance.videos.all()
        video_serializer = VideoSerializer(videos, many=True)
        return Response({
            'serial': serial_serializer.data,
            'videos': video_serializer.data
        })



class MultifilmListView(ListAPIView):
    queryset = Multifilm.objects.all()
    serializer_class = MultifilmSerializer

class MultifilmDetailView(RetrieveAPIView):
    queryset = Multifilm.objects.all()
    serializer_class = MultifilmSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serial_serializer = self.get_serializer(instance)
        videos = instance.videos.all()
        video_serializer = VideoSerializer(videos, many=True)
        return Response({
            'serial': serial_serializer.data,
            'videos': video_serializer.data
        })


from django.shortcuts import render

class CinemaJangariAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='action')

class CinemaKomediaAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='comedy')


class CinemaDramaiAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='drama')


class CinemaHorrorAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='horror')


class CinemaRomanceAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='romance')


class CinemaFantastikAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='fantastik')


class CinemaHayotiyAPIView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get_queryset(self):
        return Cinema.objects.filter(genre='hayotiy')

# Create your views here.
