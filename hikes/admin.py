from django.contrib import admin
from .models import Hike


class HikeAdmin(admin.ModelAdmin):
    list_display = (
        'difficulty',
        'title',
        'description',
        'price',
    )

    ordering = ('difficulty',)


admin.site.register(Hike, HikeAdmin)
