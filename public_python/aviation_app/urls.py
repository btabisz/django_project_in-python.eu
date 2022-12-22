
from django.urls import path
from aviation_app.views import metar_view, airports_view, taf_view, significant_view

urlpatterns = [
    path('metar/', metar_view, name='metar_view'),
    path('airports/', airports_view, name='airports_view'),
    path('taf/', taf_view, name='taf_view'),
    path('significant/', significant_view, name='significant_view'),

]
