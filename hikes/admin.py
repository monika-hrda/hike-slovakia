from django.contrib import admin
from .models import Hike


class HikeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'difficulty',
        'price',
        'image',
    )

    ordering = ('title',)


admin.site.register(Hike, HikeAdmin)
