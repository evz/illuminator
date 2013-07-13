from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

from django.contrib.gis.gdal import DataSource, OGRGeomType, OGRGeometry
from illuminator.models import TifDistrict
import os.path
from datetime import datetime

STATUS_URL = 'http://data.cityofchicago.org/resource/3qsz-jemf.json'

MULTI_TYPES = {
    1 : OGRGeomType('MultiPoint'),
    2 : OGRGeomType('MultiLineString'),
    3 : OGRGeomType('MultiPolygon'),
    OGRGeomType('Point25D').num : OGRGeomType('MultiPoint25D'),
    OGRGeomType('LineString25D').num : OGRGeomType('MultiLineString25D'),
    OGRGeomType('Polygon25D').num : OGRGeomType('MultiPolygon25D'),
}

def make_multi(geom_type, model_field):
    """
    Given the OGRGeomType for a geometry and its associated GeometryField,
    determine whether the geometry should be turned into a GeometryCollection.
    """
    return (geom_type.num in MULTI_TYPES and model_field.__class__.__name__ == 'Multi%s' % geom_type.django)

def verify_geom(geom, model_field):
    """
    Verifies the geometry -- will construct and return a GeometryCollection
    if necessary (for example if the model field is MultiPolygonField while
    the mapped shapefile only contains Polygons).
    """
                                        
    if make_multi(geom.geom_type, model_field):
        # Constructing a multi-geometry type to contain the single geometry
        multi_type = MULTI_TYPES[geom.geom_type.num]
        g = OGRGeometry(multi_type)
        g.add(geom)
    else:
        g = geom
                  
    # Returning the WKT of the geometry.
    return g.wkt

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
            tif = TifDistrict(**f)
            tif.save()

