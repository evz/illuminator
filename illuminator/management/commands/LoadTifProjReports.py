from django.core.management.base import BaseCommand, CommandError, handle_default_options
from datetime import datetime

from illuminator.models import TifProjectionReport, TifDistrict
import requests

PROJ_REPORT = 'http://data.cityofchicago.org/resource/zai4-r88e.json'

class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        proj_data = requests.get(PROJ_REPORT)
        if proj_data.status_code != 200:
            raise CommandError('City data portal returned a %s status when downloading projection reports: %s' % (proj_data.status_code, proj_data.content))
        else:
            for row in proj_data.json():
                tif = TifDistrict.objects.get(ref_number=row['tif_reference_number'])
                del row['tif_reference_number']
                del row['tif_name']
                row['tif'] = tif
                row['amount'] = int(row['amount'].replace(',',''))
                row['end_date'] = datetime.strptime(row['end_date'], '%Y-%m-%dT%H:%M:%S')
                proj_report = TifProjectionReport(**row)
                proj_report.save()
