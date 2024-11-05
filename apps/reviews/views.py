from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework.permissions import AllowAny
class ReviewsView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]


class ReviewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer