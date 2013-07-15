import logging
import json
from django.forms.widgets import Textarea
from django.template import loader, Context
from django.utils import translation
from django.contrib.gis.gdal import OGRException
logger = logging.getLogger('illuminator')

class LeafletWidget(Textarea):
    """ 
    Renders a Leaflet map using GeoJSON of the geometry
    """
    def render(self, name, value, attrs=None):
        if attrs:
            self.params.update(attrs)
        self.params['geojson'] = {}
        if value:
            srid = self.params['srid']
            if value.srid != srid:
                try:
                    ogr = value.ogr
                    ogr.transform(srid)
                    bb = ogr.extent
                    geojson = json.loads(ogr.geojson)
                except OGRException as err:
                    logger.error(
                        "Error creating geometry from value '%s' (%s)" % (
                        value, err)
                    )
                    geojson = {}
            else:
                geojson = json.loads(value.geojson)
                bb = value.extent
            bbox = ((bb[1], bb[0]),(bb[3], bb[2]),)
            geojson['properties'] = {'bbox': bbox}
        self.params['geojson'] = json.dumps(geojson)
        self.params['map_options'] = self.map_options()
        return loader.render_to_string(self.template, self.params)
    
    def map_options(self):
        return {}
