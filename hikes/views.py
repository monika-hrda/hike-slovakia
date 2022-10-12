from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def edit_hike(request, hike_id):
    """ Edit a hike """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    hike = get_object_or_404(Hike, pk=hike_id)
    if request.method == 'POST':
        form = HikeForm(request.POST, request.FILES, instance=hike)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated hike!')
            return redirect(reverse('hike_detail', args=[hike.id]))
        else:
            messages.error(request,
                           ('Failed to update hike. '
                            'Please ensure the form is valid.'))
    else:
        form = HikeForm(instance=hike)
        messages.info(request, f'You are editing {hike.title}')

    template = 'hikes/edit_hike.html'
    context = {
        'form': form,
        'hike': hike,
    }

    return render(request, template, context)


@login_required
def delete_hike(request, hike_id):
    """ Delete a hike """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    hike = get_object_or_404(Hike, pk=hike_id)
    hike.delete()
    messages.success(request, 'Hike deleted!')
    return redirect(reverse('hikes'))
