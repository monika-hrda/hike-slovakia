from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Booking
from .models import UserProfile
from .forms import UserProfileForm, UserForm


@login_required
def profile(request):
    """ Display and edit the logged in user's profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Profile update failed. Please make sure your details are valid.')

    profile_form = UserProfileForm(instance=user_profile)
    user_form = UserForm(instance=user_profile.user)
    bookings = user_profile.bookings.all()

    template = 'profiles/profile.html'
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'bookings': bookings,
    }

    return render(request, template, context)


@login_required
def booking_history(request, booking_number):
    """ A view to render details of a booking made in the past"""
    booking = get_object_or_404(Booking, booking_number=booking_number)

    messages.info(request, (
        f'This is a past confirmation for booking number {booking_number}.'
        'A confirmation email was sent on the booking date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
        'from_profile': True,
    }

    return render(request, template, context)
