from django.views.generic import ListView,DetailView
from .models import Cinema,Video,Multifilm,MultifilmVideo



class CinemaViews(ListView):
    model = Cinema,
    template_name = "cinema_list.html"

    def get_queryset(self):
        # Bu metod ListView uchun kerak, lekin biz bu yerdan foydalanmaymiz
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinemas'] = Cinema.objects.all()
        context['serials'] = Serial.objects.all()
        return context




class CinemaJangariView(ListView):
    model = Cinema
    template_name = "action.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='action')


class CinemaKomediaiView(ListView):
    model = Cinema
    template_name = "komedia.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='comedy').order_by('?')[:5]


class CinemaDramaiView(ListView):
    model = Cinema
    template_name = "drama.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='drama').order_by('?')[:5]


class CinemaHorrorView(ListView):
    model = Cinema
    template_name = "horror.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='horror')


class CinemaRomanceView(ListView):
    model = Cinema
    template_name = "romance.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='romance').order_by('?')[:5]


class CinemaFantastikView(ListView):
    model = Cinema
    template_name = "fantastik.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='fantastik')


class CinemaHayotiyView(ListView):
    model = Cinema
    template_name = "hayotiy.html"

    def get_queryset(self):
        return Cinema.objects.filter(genre='hayotiy')


class CinameJangariPage(DetailView):
    model = Cinema
    template_name = 'action_page.html'

from django.views.generic import DetailView
from .models import Serial

class SerialDetailView(DetailView):
    model = Serial
    template_name = 'serial_detail.html'


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.get_object()
        context['serial'] = video.serial
        return context


class MultifilmDetailView(DetailView):
    model = Multifilm
    template_name = 'multifilm_detail.html'

class MultifilmVideoDetailView(DetailView):
    model = MultifilmVideo
    template_name = 'multifilm_video_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.get_object()
        context['multifilm'] = video.multifilm
        context['videos'] = video.multifilm.videos.all()
        return context

