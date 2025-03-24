import django_filters
from .models import DataPoint

class DataPointFilter(django_filters.FilterSet):
    end_year = django_filters.CharFilter(field_name="end_year", lookup_expr="icontains")
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")
    topic = django_filters.CharFilter(field_name="topic", lookup_expr="icontains")
    region = django_filters.CharFilter(field_name="region", lookup_expr="icontains")
    sector = django_filters.CharFilter(field_name="sector", lookup_expr="icontains")
    source = django_filters.CharFilter(field_name="source", lookup_expr="icontains")

    class Meta:
        model = DataPoint
        fields = ['end_year', 'country', 'topic', 'region', 'sector', 'source']
