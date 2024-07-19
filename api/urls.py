from django.urls import path, re_path
from .views import (
    CinemaListView, CinemaDetailView,
    SerialListView, SerialDetailView,
    MultifilmListView, MultifilmDetailView,
    CinemaJangariAPIView, AllModelsListView, CinemaKomediaAPIView, CinemaDramaiAPIView, CinemaHorrorAPIView,
    CinemaRomanceAPIView, CinemaFantastikAPIView, CinemaHayotiyAPIView
)

urlpatterns = [
    path('', AllModelsListView.as_view(), name='all-models'),
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaDetailView.as_view(), name='cinema-detail'),
    path('serials/', SerialListView.as_view(), name='serial-list'),
    path('serials/<int:pk>/', SerialDetailView.as_view(), name='serial-detail'),
    path('multifilms/', MultifilmListView.as_view(), name='multifilm-list'),
    path('multifilms/<int:pk>/', MultifilmDetailView.as_view(), name='multifilm-detail'),
    path('drama/', CinemaDramaiAPIView.as_view(), name='jangari-list'),
    path('horror/', CinemaHorrorAPIView.as_view(), name='jangari-list'),
    path('ronce/', CinemaRomanceAPIView.as_view(), name='jangari-list'),
    path('fantastik/', CinemaFantastikAPIView.as_view(), name='jangari-list'),
    path('hayotiy/', CinemaHayotiyAPIView.as_view(), name='jangari-list'),
    path('komedia/', CinemaKomediaAPIView.as_view(), name='jangari-list'),
    path('jangari/', CinemaJangariAPIView.as_view(), name='jangari-list'),

]
