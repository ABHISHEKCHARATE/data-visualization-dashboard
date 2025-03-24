from django.urls import path
from .views import DataPointListView , dashboard_view

urlpatterns = [
    path('api/data/', DataPointListView.as_view(), name='data-list'),
    path('', dashboard_view, name='dashboard'),

]
