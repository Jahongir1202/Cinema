from django.shortcuts import render
from django.views.generic import ListView
from .models import Cinema

class CinemaViews(ListView):
    model = Cinema
    template_name = "cinema_list.html"


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
