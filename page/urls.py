from django.urls import path
from .views import (
    CinemaViews,
    CinemaJangariView,
    CinemaHayotiyView,
    CinemaKomediaiView,
    CinemaFantastikView,
    CinemaDramaiView,
    CinemaHorrorView,
    CinemaRomanceView,
    CinameJangariPage,
    SerialDetailView,
    VideoDetailView,
    MultifilmDetailView,
    MultifilmVideoDetailView,
)
#ozgardi
urlpatterns = [
    path('',CinemaViews.as_view(),name = 'home'),
    path('jangari/',CinemaJangariView.as_view(),name='jangari'),
    path('komedia/', CinemaKomediaiView.as_view(), name='komedia'),
    path('drama/', CinemaDramaiView.as_view(), name='drama'),
    path('fantastik/', CinemaFantastikView.as_view(), name='fantastik'),
    path('horror/', CinemaHorrorView.as_view(), name='horror'),
    path('romance/', CinemaRomanceView.as_view(), name='romance'),
    path('hayotiy/',CinemaHayotiyView.as_view(),name='hayotiy'),
    path('serial/<int:pk>/', SerialDetailView.as_view(), name='serial_detail'),
    path('<int:pk>/action/',CinameJangariPage.as_view(),name='pagejangari'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('multifilm/<int:pk>/', MultifilmDetailView.as_view(), name='multifilm_detail'),
    path('multifilm_video/<int:pk>/', MultifilmVideoDetailView.as_view(), name='multifilm_video_detail'),
    # path('cinema/<int:cinema_id>/', cinema_detail(), name='cinema_detail'),  # Yangi URL

]
