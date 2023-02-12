from rest_framework import status
from watchlist_app.models import Watchlist
from .slzr import WatchlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def watchlist(request):
    if request.method == 'GET':
        data = Watchlist.objects.all()
        slzr = WatchlistSerializer(data, many=True)
        return Response(slzr.data)
    if request.method == 'POST':
        slzr = WatchlistSerializer(data=request.data, many=True)
        if slzr.is_valid():
            slzr.save()
            return Response(slzr.data)
        else:
            return Response(slzr.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def watchlist_detail(request, pk):
    if request.method == 'GET':
        try:
            data = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error':"Watchlist Does Not Exist"},status=status.HTTP_404_NOT_FOUND)
        slzr = WatchlistSerializer(data)
        return Response(slzr.data)
    if request.method == 'PUT':
        watchlist = Watchlist.objects.get(pk=pk)
        slzr = WatchlistSerializer(watchlist,data=request.data)
        if slzr.is_valid():
            slzr.save()
            return Response(slzr.data)
        else:
            return Response(slzr.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        data = Watchlist.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
