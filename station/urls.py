from django.urls import path

from station import views

app_name = 'station'

urlpatterns = [
    path('', views.stations_view, name='stations'),
    path('<int:station_id>/', views.station_view, name='station'),

    path('titles/', views.titles_view, name='titles'),
]
