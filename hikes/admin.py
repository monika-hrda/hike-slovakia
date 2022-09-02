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
    # readonly_fields = ('hike', 'date',)
    list_display = ('date', 'hike')
    list_filter = ('hike', 'date')

    # credit https://stackoverflow.com/questions/52539923/how-to-make-non-editable-fields-appear-when-creating-objects-in-django-admin
    def get_readonly_fields(self, request, obj=None):
        defaults = super().get_readonly_fields(request, obj=obj)
        if obj:  # if we are updating an object
            defaults = tuple(defaults) + ('hike', 'date', )  # make sure defaults is a tuple
        return defaults


admin.site.register(Hike, HikeAdmin)
admin.site.register(ScheduledHike, ScheduledHikeAdmin)
