from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, UserForm


def profile(request):
    """ Display the user's profile """
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
