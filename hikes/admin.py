from django.contrib import admin
from .models import Hike, ScheduledHike


class HikeAdmin(admin.ModelAdmin):
    """ Admin for Hike model """
    list_display = (
        'title',
        'difficulty',
        'price',
        'image',
    )

    ordering = ('title',)


class ScheduledHikeAdmin(admin.ModelAdmin):
    """ Admin for ScheduledHike model """
    list_display = ('date', 'hike')
    list_filter = ('hike', 'date')

    # credit in README.md
    def get_readonly_fields(self, request, obj=None):
        defaults = super().get_readonly_fields(request, obj=obj)
        if obj:  # if we are updating an object
            # make sure defaults is a tuple
            defaults = tuple(defaults) + ('hike', 'date', )
        return defaults


admin.site.register(Hike, HikeAdmin)
admin.site.register(ScheduledHike, ScheduledHikeAdmin)
