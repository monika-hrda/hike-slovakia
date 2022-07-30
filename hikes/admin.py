from django.contrib import admin
from .models import Hike


class HikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hike, HikeAdmin)
