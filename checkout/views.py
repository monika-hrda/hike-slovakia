from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from localStoragePy import localStoragePy
from hikes.models import Hike


def view_basket(request, hike_id):

    hike = get_object_or_404(Hike, pk=hike_id)

    hike_date = None
    if 'hike_date' in request.POST:
        hike_date = request.POST['hike_date']
    if not hike_date:
        messages.error(request, "There is nothing to book at the moment")
        return redirect(reverse('hikes'))

    num_hikers = 1
    if 'number_of_people' in request.POST:
        num_hikers = request.POST['number_of_people']

    price_total = Decimal(hike.price) * Decimal(num_hikers)

    local_storage = localStoragePy('hike-slovakia', 'json')
    local_storage.setItem('hike_date', hike_date)
    local_storage.setItem('num_hikers', num_hikers)
    local_storage.setItem('price_total', price_total)
    local_storage.setItem('hike_id', hike_id)

    template = 'checkout/basket.html'
    context = {
        'hike': hike,
        'hike_date': hike_date,
        'num_hikers': num_hikers,
        'price_total': price_total,
    }

    return render(request, template, context)
