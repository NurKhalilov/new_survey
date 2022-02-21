from rate.models import Salesperson, Rating
from rest_framework import generics
from .serializers import RatingSerializer
# Create your views here.

class RatingList(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
class RatingDetail(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
