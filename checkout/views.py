from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from localStoragePy import localStoragePy
import stripe
from hikes.models import Hike


def view_basket(request, hike_id):

    hike = get_object_or_404(Hike, pk=hike_id)

    hike_date = request.POST.get('hike_date')
    if not hike_date:
        messages.error(request, "There is nothing to book at the moment")
        return redirect(reverse('hikes'))

    num_hikers = request.POST.get('number_of_people', '1')

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


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    local_storage = localStoragePy('hike-slovakia', 'json')

    hike_id = local_storage.getItem('hike_id')
    if not hike_id:
        messages.error(request, "There is nothing to book at the moment")
        return redirect(reverse('hikes'))
    hike_date = local_storage.getItem('hike_date')
    num_hikers = int(local_storage.getItem('num_hikers'))
    price_total = Decimal(local_storage.getItem('price_total'))

    hike = get_object_or_404(Hike, pk=hike_id)

    if request.method == 'POST':
        pass

    else:
        stripe_total = round(price_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'hike': hike,
        'hike_date': hike_date,
        'num_hikers': num_hikers,
        'price_total': price_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
