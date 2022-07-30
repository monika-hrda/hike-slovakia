from django.shortcuts import render
from .models import Hike


def all_hikes(request):
    """ A view to show all hikes """

    hikes = Hike.objects.all()

    context = {
        'hikes': hikes,
    }

    return render(request, 'hikes/hikes.html', context)
