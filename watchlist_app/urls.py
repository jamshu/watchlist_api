
from django.urls import path,include
from .views import get_watchlist
urlpatterns = [
    path('',get_watchlist,name='watchlist')
]