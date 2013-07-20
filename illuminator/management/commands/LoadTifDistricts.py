from django.core.management.base import BaseCommand, CommandError, handle_default_options

from django.contrib.gis.gdal import DataSource, OGRGeomType, OGRGeometry
from illuminator.models import TifDistrict
import os
import zipfile
from cStringIO import StringIO
import requests
from datetime import datetime
from utils import verify_geom

SHP = 'https://data.cityofchicago.org/api/geospatial/fz5x-7zak?method=export&format=Shapefile'

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
            'REF': 'ref_number',
        }
        shp_data = requests.get(SHP)
        if shp_data.status_code != 200:
            raise CommandError('City data portal returned a %s status when downloading TIFs shapefile: %s' % (shp_data.status_code, shp_data.content))
        else:
            s = StringIO(shp_data.content)
            z = zipfile.ZipFile(s)
            fname = [f for f in z.namelist() if f.endswith('shp')][0]
            data_path = os.path.join(os.path.curdir,'data/shp/tifs')
            z.extractall(data_path)
            shpfile = os.path.join(data_path,fname)
            data_layer = DataSource(shpfile)[0]
            for feat in data_layer:
                f = {}
                for k in mapping.keys():
                    if 'date' in mapping.get(k):
                        if feat.get(k):
                            f[mapping.get(k)] = datetime.strptime(feat.get(k), '%m/%d/%Y')
                        else:
                            f[mapping.get(k)] = None
                    elif mapping.get(k) == 'ref_number':
                        print feat.get('REF')
                        ref_number = '-'.join([feat.get('REF').split('-')[0], str(int(feat.get('REF').split('-')[1])).zfill(3)])
                        print ref_number
                        f['ref_number'] = ref_number
                    else:
                        f[mapping.get(k)] = feat.get(k)
                f['geom'] = verify_geom(feat.geom, TifDistrict._meta.get_field('geom'))
                tif = TifDistrict(**f)
                tif.save()

