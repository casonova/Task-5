from django.core.management.base import BaseCommand
from customer.models import Customer
from datetime import datetime


class Command(BaseCommand):
    help = "Create 100 customers in database"
    
    def handle(self, *args, **kwargs):
        current_time = datetime.utcnow()
        
        for i in range(100):
            customer_name = f"Customer name {i}"
            Customer.objects.create(name=customer_name, Time=current_time, is_utc=True, is_pst=False)
