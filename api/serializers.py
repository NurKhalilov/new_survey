from rest_framework import serializers
from rate.models import Salesperson, Rating


class RatingSerializer(serializers.ModelSerializer):
    salername = serializers.CharField(source='salesperson.name', read_only=True)
    class Meta:
        model = Rating
        fields = ('id', 'salername', 'rating')