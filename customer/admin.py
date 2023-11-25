from django.contrib import admin
from django.utils import timezone

from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "Time", "is_utc", "is_pst"]
    ordering = ["id"]
