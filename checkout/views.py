from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from hikes.models import Hike


def checkout(request, hike_id):

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

    price_total = float(hike.price) * float(num_hikers)

    # order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'hike': hike,
        'hike_date': hike_date,
        'num_hikers': num_hikers,
        'price_total': price_total,
        # 'order_form': order_form,
    }

    return render(request, template, context)
