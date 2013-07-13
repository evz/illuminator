{% extends "gis/admin/openlayers.js" %}
{% block base_layer %}new OpenLayers.Layer.OSM("OpenStreetMap (Mapnik)", 'http://otile1.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png');{% endblock %}
