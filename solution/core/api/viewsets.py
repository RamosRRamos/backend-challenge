from rest_framework import viewsets, permissions

from core.api.serializers import PlaceSerializer
from core.models import Place


class PlaceViewSet(viewsets.ModelViewSet):

    queryset = Place.objects.all().order_by('-name')
    serializer_class = PlaceSerializer
