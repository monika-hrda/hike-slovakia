from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from localStoragePy import localStoragePy
import stripe
from hikes.models import Hike, ScheduledHike
from profiles.models import UserProfile
from .models import Booking


def _get_hike_date_from_id(hike_date_id):
    try:
        hike_date = ScheduledHike.objects.get(id=hike_date_id).date
    except ScheduledHike.DoesNotExist:
        hike_date = None

    return hike_date


@login_required
def view_basket(request, hike_id):

    hike = get_object_or_404(Hike, pk=hike_id)

    hike_date_id = request.POST.get('hike_date_id')
    if not hike_date_id:
        messages.error(request, "There is nothing to book at the moment")
        return redirect(reverse('hikes'))

    num_hikers = request.POST.get('number_of_people', '1')

    price_total = Decimal(hike.price) * Decimal(num_hikers)

    local_storage = localStoragePy('hike-slovakia', 'json')
    local_storage.setItem('hike_date_id', hike_date_id)
    local_storage.setItem('num_hikers', num_hikers)
    local_storage.setItem('price_total', price_total)
    local_storage.setItem('hike_id', hike_id)

    hike_date = _get_hike_date_from_id(hike_date_id)

    template = 'checkout/basket.html'
    context = {
        'hike': hike,
        'hike_date': hike_date,
        'num_hikers': num_hikers,
        'price_total': price_total,
    }

    return render(request, template, context)


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    local_storage = localStoragePy('hike-slovakia', 'json')

    hike_id = local_storage.getItem('hike_id')
    if not hike_id:
        messages.error(request, "There is nothing to book at the moment")
        return redirect(reverse('hikes'))
    hike_date_id = local_storage.getItem('hike_date_id')
    num_hikers = int(local_storage.getItem('num_hikers'))
    price_total = Decimal(local_storage.getItem('price_total'))

    hike_date = _get_hike_date_from_id(hike_date_id)

    try:
        hike = Hike.objects.get(pk=hike_id)
    except Hike.DoesNotExist:
        messages.error(request, (
            "The requested hike wasn't found in our database. "
            "Please call us for assistance!")
        )
        return redirect(reverse('hikes'))

    if request.method == 'POST':
        user_profile = get_object_or_404(UserProfile, user=request.user)
        booking = Booking.objects.create(
            user_profile=user_profile,
            hike=hike, hike_date=hike_date,
            num_hikers=num_hikers, price_total=price_total
        )
        booking.save()
        send_confirmation_email(booking)
        return redirect(reverse('checkout_success', args=[booking.booking_number]))

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


@login_required
def checkout_success(request, booking_number):
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Booking successfully processed! \
        Your booking number is {booking_number}. \
        We are looking forward to meeting you on {booking.hike_date}.')

    localStoragePy('hike-slovakia', 'json').clear()

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)


def send_confirmation_email(booking):
    """Send the user a confirmation email"""
    cust_email = booking.user_profile.user.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'booking': booking})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'booking': booking, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
