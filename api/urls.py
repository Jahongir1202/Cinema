from django.urls import path
from .views import (
    CinemaListView, CinemaDetailView,
    SerialListView, SerialDetailView,
    VideoListView, VideoDetailView,
    MultifilmListView, MultifilmDetailView,
    MultifilmVideoListView, MultifilmVideoDetailView
)

urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaDetailView.as_view(), name='cinema-detail'),
    path('serials/', SerialListView.as_view(), name='serial-list'),
    path('serials/<int:pk>/', SerialDetailView.as_view(), name='serial-detail'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('multifilms/', MultifilmListView.as_view(), name='multifilm-list'),
    path('multifilms/<int:pk>/', MultifilmDetailView.as_view(), name='multifilm-detail'),
    path('multifilm-videos/', MultifilmVideoListView.as_view(), name='multifilm-video-list'),
    path('multifilm-videos/<int:pk>/', MultifilmVideoDetailView.as_view(), name='multifilm-video-detail'),
]
