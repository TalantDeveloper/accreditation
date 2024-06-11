from django.shortcuts import render

from main.function import get_context
from station.models import Station, Title


def stations_view(request):
    context = get_context(request)

    return render(request, 'station/stations.html', context)


def station_view(request, station_id):
    context = get_context(request)
    context['station'] = Station.objects.get(pk=station_id)
    return render(request, 'station/station.html', context)


def titles_view(request):
    context = get_context(request)
    context['titles'] = Title.objects.all()

    return render(request, 'station/titles.html', context)
