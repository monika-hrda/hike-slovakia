from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Hike, ScheduledHike
from .forms import HikeForm


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


def add_hike(request):
    """ A view to add a new hike """

    if request.user.is_superuser:
        if request.method == 'POST':
            form = HikeForm(request.POST, request.FILES)
            if form.is_valid():
                hike = form.save()
                messages.success(request, 'Successfully added hike!')
                return redirect(reverse('hike_detail', args=[hike.id]))
            else:
                messages.error(request,
                               ('Failed to add hike. '
                                'Please ensure the form is valid.'))
        else:
            form = HikeForm()

        template = 'hikes/add_hike.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
    return render(request, 'home/index.html')
