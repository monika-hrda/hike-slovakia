from django.db import models
from hikes.models import Hike


class Booking(models.Model):
    # user = models.ForeignKey(UserProfile,
    #                         on_delete=models.CASCADE,
    #                         related_name='user_bookings')
    hike = models.ForeignKey(Hike,
                             on_delete=models.CASCADE,
                             related_name='hike_bookings')
    hike_date = models.DateField()
    num_hikers = models.IntegerField(null=False, blank=False, default=1)
    price_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, blank=False, editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.user} booked {self.hike}'
