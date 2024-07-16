from django.urls import path
from .views import (
    CinemaViews,
    CinemaJangariView,
    CinemaHayotiyView,
    CinemaKomediaiView,
    CinemaFantastikView,
    CinemaDramaiView,
    CinemaHorrorView,
    CinemaRomanceView
)

urlpatterns = [
    path('',CinemaViews.as_view(),name = 'home'),
    path('jangari/',CinemaJangariView.as_view(),name='jangari'),
    path('komedia/', CinemaKomediaiView.as_view(), name='komedia'),
    path('drama/', CinemaDramaiView.as_view(), name='drama'),
    path('fantastik/', CinemaFantastikView.as_view(), name='fantastik'),
    path('horror/', CinemaHorrorView.as_view(), name='horror'),
    path('romance/', CinemaRomanceView.as_view(), name='romance'),
    path('hayotiy/',CinemaHayotiyView.as_view(),name='hayotiy'),

]
