from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

from django.contrib.gis.gdal import DataSource, OGRGeomType, OGRGeometry
from illuminator.models import TifDistrict
import os.path
import json
from datetime import datetime
from utils import verify_geom

class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        mapping = {
            'NAME': 'name',
            'IND': 'ind',
            'TYPE': 'type',
            'USE': 'use',
            'REPEALED_D': 'repealed_date',
            'APPROVAL_D': 'approval_date',
            'EXPIRATION': 'expiration_date',
        }
        datafile = os.path.join(os.path.curdir,'data/shp/tifs/TIF_Districts.shp')
        xref = open(os.path.join(os.path.curdir, 'data/xref.json'), 'rb')
        tif_id_ref = json.loads(xref.read())
        data_layer = DataSource(datafile)[0]
        for feat in data_layer:
            f = {}
            for k in mapping.keys():
                if 'date' in mapping.get(k):
                    if feat.get(k):
                        f[mapping.get(k)] = datetime.strptime(feat.get(k), '%m/%d/%Y')
                    else:
                        f[mapping.get(k)] = None
                else:
                    f[mapping.get(k)] = feat.get(k)
            f['geom'] = verify_geom(feat.geom, TifDistrict._meta.get_field('geom'))
            f['ref_number'] = tif_id_ref[f['name']]
            tif = TifDistrict(**f)
            tif.save()

