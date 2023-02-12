
from django.urls import path,include
from .views import WatchlistAV,WatchlistDetailAV
urlpatterns = [
    path('',WatchlistAV.as_view(),name='watchlist'),
    path('<int:pk>/',WatchlistDetailAV.as_view(),name='watchlist_detail'),


]