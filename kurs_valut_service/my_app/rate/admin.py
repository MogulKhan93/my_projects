from django.contrib import admin
from .models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ('rate_name', 'official_rate')
    search_fields = ('rate_name',)


admin.site.register(Rate, RateAdmin)
