from django.shortcuts import render, get_object_or_404
from .models import Hike, ScheduledHike


def all_hikes(request):
    """ A view to show all hikes """

    hikes = Hike.objects.all()

    context = {
        'hikes': hikes,
    }

    return render(request, 'hikes/hikes.html', context)


def hike_detail(request, hike_id):
    """ A view to show individual hike details """

    hike = get_object_or_404(Hike, pk=hike_id)
    scheduled_hikes = ScheduledHike.objects.filter(hike=hike).order_by('date')

    context = {
        'hike': hike,
        'scheduled_hikes': scheduled_hikes,
    }

    return render(request, 'hikes/hike_detail.html', context)
