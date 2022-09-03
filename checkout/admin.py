from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'hike',
                    'hike_date', 'num_hikers',
                    'price_total',)

    readonly_fields = ('payment_date', 'price_total',)

    ordering = ('-payment_date',)


admin.site.register(Booking, BookingAdmin)
