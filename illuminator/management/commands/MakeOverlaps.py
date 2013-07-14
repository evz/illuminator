from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

from django.contrib.gis.gdal import OGRGeometry
from illuminator.models import TifDistrict, Ward, Overlap
from utils import verify_geom

class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        wards = Ward.objects.all()
        for ward in wards:
            tifs = TifDistrict.objects.filter(geom__overlaps=ward.geom)
            for tif in tifs:
                shape = OGRGeometry(ward.geom.intersection(tif.geom).wkt)
                overlap_geom = verify_geom(shape, Overlap._meta.get_field('overlap'))
                overlap = Overlap(ward=ward, tif=tif, overlap=overlap_geom)
                overlap.save()

