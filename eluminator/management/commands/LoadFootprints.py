"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

from django.contrib.gis.utils import LayerMapping
from core.models import Footprint
import os.path
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        mapping = {
         'active_date': 'BLDG_ACTIV',
         'building_id': 'BLDG_ID',
         'cdb_city_i': 'CDB_CITY_I',
         'comments': 'COMMENTS',
         'condition': 'BLDG_CONDI',
         'condition_date': 'CONDITION_',
         'create_date': 'BLDG_CREAT',
         'create_user': 'CREATE_USE',
         'demolished': 'DEMOLISHED',
         'edit_date': 'EDIT_DATE',
         'edit_source': 'EDIT_SOURC',
         'edit_userid': 'EDIT_USERI',
         'end_date': 'BLDG_END_D',
         'footprint_field': 'FOOTPRINT_',
         'from_address': 'F_ADD1',
         'harris_str': 'HARRIS_STR',
         'label_hous': 'LABEL_HOUS',
         'name1': 'BLDG_NAME1',
         'name2': 'BLDG_NAME2',
         'no_of_units': 'NO_OF_UNIT',
         'no_stories': 'NO_STORIES',
         'non_standard': 'NON_STANDA',
         'orig_bldg_field': 'ORIG_BLDG_',
         'qc_date': 'QC_DATE',
         'qc_source': 'QC_SOURCE',
         'qc_userid': 'QC_USERID',
         'shape_area': 'SHAPE_AREA',
         'shape_len': 'SHAPE_LEN',
         'square_footage': 'BLDG_SQ_FO',
         'status': 'BLDG_STATU',
         'stories': 'STORIES',
         'street_name': 'ST_NAME1',
         'street_prefix': 'PRE_DIR1',
         'street_type': 'ST_TYPE1',
         'suffix_dir': 'SUF_DIR1',
         'to_address': 'T_ADD1',
         'unit_name': 'UNIT_NAME',
         'vacancy_status': 'VACANCY_ST',
         'x_coord': 'X_COORD',
         'y_coord': 'Y_COORD',
         'year_built': 'YEAR_BUILT',
         'z_coord': 'Z_COORD',
         'geom': 'MULTIPOLYGON'
         }
         # The mapping is a dictionary
        datafile = os.path.join(os.path.curdir,'data/Building_Footprints/Buildings.shp')
        lm = LayerMapping(Footprint, datafile, mapping)
        lm.save(strict=True,progress=True,fid_range=(1,1000)) # Save the layermap, imports the data.
        print "Only loaded 1000 right now don't be fooled!"


