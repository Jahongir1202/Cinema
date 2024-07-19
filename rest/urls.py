from django.urls import path
from rest.views import MoviaCinemaView, VideoCinemaView, MoviaSerialView, VideoSerialView, MoviaMultifilmView, \
    VideoMultifilmView, MoviaAllView

urlpatterns = [
    path('', MoviaAllView.as_view(), name='movia_all'),
    path('cinema/', MoviaCinemaView.as_view(), name='cinema'),
    path('cinema/<int:pk>/', VideoCinemaView.as_view(), name='id_cinema'),
    path('serial/', MoviaSerialView.as_view(), name='serial'),
    path('serial/<int:pk>/', VideoSerialView.as_view(), name='id_serial'),
    path('multifilm/', MoviaMultifilmView.as_view(), name='multifilm'),
    path('multifilm/<int:pk>/', VideoMultifilmView.as_view(), name='id_multifilm'),
]
