from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import DataPoint
from .serializers import DataPointSerializer
from .filters import DataPointFilter

class DataPointListView(generics.ListAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DataPointFilter



from django.shortcuts import render

def dashboard_view(request):
    return render(request, "index.html")

