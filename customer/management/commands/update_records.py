from django.core.management.base import BaseCommand
from customer.models import Customer
import pytz
from datetime import datetime
import os
from django.utils import timezone
from cronjob_task.settings import BASE_DIR
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Update recorded time of customers every 5 minutes in alternating timezones"

    def handle(self, *args, **kwargs):
        records_fetch = 10
        count = self.read_count()

        if (Customer.objects.filter(is_utc=False).count() == count and count<100) or Customer.objects.filter(is_utc=True).count() == count:
            fetched_records = Customer.objects.filter(is_utc=True)[:records_fetch]
            for record in fetched_records:
                utc_time = record.Time
                pst_time = utc_time.astimezone(pytz.timezone('Asia/Karachi'))
                record.Time = pst_time
                record.is_utc = False
                record.is_pst = True
                record.save()
                logger.info(f"Customer {record.id} time updated in pst format {record.Time}")
            self.update_count(count)

        elif (Customer.objects.filter(is_pst = False).count() == count and count<100) or Customer.objects.filter(is_pst = True).count() == count:
            fetched_records = Customer.objects.filter(is_utc=False)[:records_fetch]
            for record in fetched_records:
                pst_time = record.Time
                print(f"Customer time before updating {record.id}: {record.Time}")
                utc_time = pst_time.astimezone(pytz.utc)
                record.Time = utc_time
                record.is_utc = True
                record.is_pst=False
                record.save()
                logger.info(f"Customer {record.id} time updated in utc format {record.Time}")
            self.update_count(count)
            
    def read_count(self):
        iteration_file_path = os.path.join(BASE_DIR, "CountIteration.txt")
        with open(iteration_file_path, "r") as f:
            return int(f.read())

    def update_count(self, count):
        iteration_file_path = os.path.join(BASE_DIR, "CountIteration.txt")

        if count < 100:
            count += 10
        else:
            count = 0

        with open(iteration_file_path, "w") as f:
            f.write(str(count))
