"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

from django.contrib.gis.utils import LayerMapping
from eluminator.models import Ward
import os.path
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        mapping = {
            'perimeter': 'PERIMETER',
            'ward': 'WARD',
            'alderman': 'ALDERMAN',
            'ward_phone': 'WARD_PHONE',
            'hall_phone': 'HALL_PHONE',
            'hall_office': 'HALL_OFFIC',
            'address': 'ADDRESS',
            'edit_date1': 'EDIT_DATE1',
            'shape_area': 'SHAPE_AREA',
            'shape_len': 'SHAPE_LEN',
            'geom': 'MULTIPOLYGON'
         }
         # The mapping is a dictionary
        datafile = os.path.join(os.path.curdir,'data/Wards.shp')
        lm = LayerMapping(Ward, datafile, mapping)
        lm.save(strict=True,progress=True)

