import json

from django.shortcuts import render
from .models import Watchlist
from django.http import JsonResponse


def get_watchlist(request):
    watchlist = Watchlist.objects.all()
    data = {'watchlist': list(watchlist.values())}
    return JsonResponse(data)

