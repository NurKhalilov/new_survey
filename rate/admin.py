from django.contrib import admin
from .models import Salesperson, Rating, Region
from import_export.admin import ExportActionMixin


@admin.register(Salesperson)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'region')


@admin.register(Rating)
class RatingAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('salesperson', 'rating', 'price', 'sent_time')
    list_filter = ('salesperson',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
