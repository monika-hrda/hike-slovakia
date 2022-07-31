from django.contrib import admin
from .models import Hike, ScheduledHike


class HikeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'difficulty',
        'price',
        'image',
    )

    ordering = ('title',)


class ScheduledHikeAdmin(admin.ModelAdmin):
    list_display = ('date', 'hike')


admin.site.register(Hike, HikeAdmin)
admin.site.register(ScheduledHike, ScheduledHikeAdmin)
