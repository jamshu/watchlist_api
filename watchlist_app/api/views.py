from watchlist_app.models import Watchlist
from .slzr import WatchlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def watchlist(request):
    data = Watchlist.objects.all()
    slzr = WatchlistSerializer(data,many=True)
    return Response(slzr.data)
@api_view()
def watchlist_detail(request,pk):
    data = Watchlist.objects.get(pk=pk)
    slzr = WatchlistSerializer(data)
    return Response(slzr.data)
