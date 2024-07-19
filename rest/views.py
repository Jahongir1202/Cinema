from rest_framework.generics import  RetrieveAPIView
from .serializers import MoviaVideoSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Movia
from .serializers import MoviaAPISerializer

class MoviaAllView(ListAPIView):
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        # Barcha `Movia` obyektlarini qaytarish
        return Movia.objects.all()

    def list(self, request, *args, **kwargs):
        # Har bir turdagi ob'ektlardan oxirgi 5 ta yoki mavjud bo'lganini olish
        cinema_movies = Movia.objects.filter(type='cinema').order_by('-id')[:5]
        serials = Movia.objects.filter(type='serial').order_by('-id')[:5]
        multifilms = Movia.objects.filter(type='multifilm').order_by('-id')[:5]

        # Serializatorlar
        cinema_serializer = self.get_serializer(cinema_movies, many=True)
        serial_serializer = self.get_serializer(serials, many=True)
        multifilm_serializer = self.get_serializer(multifilms, many=True)

        # Natijani qaytarish
        response = {
            'cinema': cinema_serializer.data,
            'serial': serial_serializer.data,
            'multifilm': multifilm_serializer.data
        }

        return Response(response)

#endAll
# Cinema
class MoviaCinemaView(ListAPIView):
    queryset = Movia.objects.all()
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        queryset = Movia.objects.filter(type='cinema')
        return queryset.order_by('-id')


class VideoCinemaView(RetrieveAPIView):
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        return Movia.objects.filter(type='cinema')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serial_serializer = self.get_serializer(instance)
        videos = instance.videos.all()
        video_serializer = MoviaVideoSerializer(videos, many=True)

        return Response({
            'movia': serial_serializer.data,
            'videos': video_serializer.data
        })

# End Cinema

# Serial
class MoviaSerialView(ListAPIView):
    queryset = Movia.objects.filter(type='serial').order_by('-id')
    serializer_class = MoviaAPISerializer

class VideoSerialView(RetrieveAPIView):
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        return Movia.objects.filter(type='serial')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serial_serializer = self.get_serializer(instance)
        videos = instance.videos.all()
        video_serializer = MoviaVideoSerializer(videos, many=True)

        return Response({
            'movia': serial_serializer.data,
            'videos': video_serializer.data
        })
# End Serial

# Multifilm
class MoviaMultifilmView(ListAPIView):
    queryset = Movia.objects.all()
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        queryset = Movia.objects.filter(type='multifilm')
        return queryset.order_by('-id')

class VideoMultifilmView(RetrieveAPIView):
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        return Movia.objects.filter(type='multifilm')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        movia_serializer = self.get_serializer(instance)
        videos = instance.videos.all()
        video_serializer = MoviaVideoSerializer(videos, many=True)

        return Response({
            'movia': movia_serializer.data,
            'videos': video_serializer.data
        })
# End Multifilm

class MoviaJangariView(ListAPIView):
    queryset = Movia.objects.filter(genre='jangari').order_by('-id')
    serializer_class = MoviaAPISerializer


class MoviakomediaView(ListAPIView):
    queryset = Movia.objects.filter(genre='komedia').order_by('-id')
    serializer_class = MoviaAPISerializer


class MoviaDramaView(ListAPIView):
    queryset = Movia.objects.filter(genre='drama').order_by('-id')
    serializer_class = MoviaAPISerializer

class MoviaUjasView(ListAPIView):
    queryset = Movia.objects.filter(genre='ujas').order_by('-id')
    serializer_class = MoviaAPISerializer

class MoviaRomanceView(ListAPIView):
    queryset = Movia.objects.filter(genre='romance').order_by('-id')
    serializer_class = MoviaAPISerializer

class MoviaFantastikView(ListAPIView):
    queryset = Movia.objects.filter(genre='fantastik').order_by('-id')
    serializer_class = MoviaAPISerializer


class MoviaHayotiyView(ListAPIView):
    queryset = Movia.objects.filter(genre='hayotiy').order_by('-id')
    serializer_class = MoviaAPISerializer


class MoviaSearchView(ListAPIView):
    serializer_class = MoviaAPISerializer

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Movia.objects.filter(title__icontains=query).order_by('-title','hashtag')