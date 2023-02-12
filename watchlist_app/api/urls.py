
from django.urls import path,include
from .views import watchlist,watchlist_detail
urlpatterns = [
    path('',watchlist,name='watchlist'),
    path('<int:pk>/',watchlist_detail,name='watchlist_detail'),


]