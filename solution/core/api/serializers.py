from rest_framework.serializers import ModelSerializer

from core.models import Place


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'slug', 'city', 'state')
