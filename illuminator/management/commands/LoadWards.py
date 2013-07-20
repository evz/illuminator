from django.core.management.base import BaseCommand, CommandError, handle_default_options

from django.contrib.gis.utils import LayerMapping
from illuminator.models import Ward
import os
import zipfile
from cStringIO import StringIO
import requests

SHP = 'https://data.cityofchicago.org/api/geospatial/xt4z-bnwh?method=export&format=Shapefile'

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
        shp_data = requests.get(SHP)
        if shp_data.status_code != 200:
            raise CommandError('City data portal returned a %s status when downloading Wards shapefile: %s' % (shp_data.status_code, shp_data.content))
        else:
            s = StringIO(shp_data.content)
            z = zipfile.ZipFile(s)
            data_path = os.path.join(os.path.curdir,'data/shp/wards')
            fname = [f for f in z.namelist() if f.endswith('shp')][0]
            z.extractall(data_path)
            datafile = os.path.join(data_path, fname)
            lm = LayerMapping(Ward, datafile, mapping)
            lm.save(strict=True,progress=True)

