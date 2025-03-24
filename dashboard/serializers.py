from rest_framework import serializers
from .models import DataPoint

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = [
            'intensity', 'likelihood', 'relevance', 'end_year',
            'country', 'topic', 'region', 'city'
        ]
