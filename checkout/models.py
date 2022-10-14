import uuid  # used to generate the booking number

from django.db import models
from hikes.models import Hike
from profiles.models import UserProfile


class Booking(models.Model):
    """
    A model to record users' bookings.
    Generates a booking number on each new order.
    Links to a user and a hike booked.
    """
    booking_number = models.CharField(max_length=32,
                                      null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='bookings')
    hike = models.ForeignKey(Hike,
                             on_delete=models.CASCADE,
                             related_name='hike_bookings')
    hike_date = models.DateField()
    num_hikers = models.IntegerField(null=False, blank=False, default=1)
    price_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, blank=False, editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def _generate_booking_number(self):
        """
        Generates a random, unique booking number using UUID,
        a random string of 32 characters
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the booking number
        if it hasn't been set already
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number
