from sys import path_hooks
from unittest.mock import patch

from django.urls import path

from api.views import AllModelsListView
from rest.views import MoviaCinemaView, VideoCinemaView, MoviaSerialView, VideoSerialView, MoviaMultifilmView, \
    VideoMultifilmView, MoviaAllView, MoviaJangariView, MoviaHayotiyView, MoviaDramaView, MoviaUjasView, \
    MoviaRomanceView, MoviaFantastikView, MoviakomediaView, MoviaSearchView

urlpatterns = [
    path('',MoviaAllView.as_view(),name='all'),
    path('cinema/', MoviaCinemaView.as_view(), name='cinema'),
    path('cinema/<int:pk>/', VideoCinemaView.as_view(), name='id_cinema'),
    path('serial/', MoviaSerialView.as_view(), name='serial'),
    path('serial/<int:pk>/', VideoSerialView.as_view(), name='id_serial'),
    path('multifilm/', MoviaMultifilmView.as_view(), name='multifilm'),
    path('multifilm/<int:pk>/', VideoMultifilmView.as_view(), name='id_multifilm'),
    path('jangari/',MoviaJangariView.as_view(),name='jangari'),
    path('komedia/', MoviakomediaView.as_view(), name='komedia'),
    path('drama/', MoviaDramaView.as_view(), name='drama'),
    path('ujas/', MoviaUjasView.as_view(), name='ujas'),
    path('romance/', MoviaRomanceView.as_view(), name='romance'),
    path('fantastik/', MoviaFantastikView.as_view(), name='fantastik'),
    path('hayotiy/', MoviaHayotiyView.as_view(), name='hayotiy'),
    path('search/',MoviaSearchView.as_view(),name='search')

]
