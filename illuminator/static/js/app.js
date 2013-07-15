(function(){
    var map;
    $(document).ready(function(){
        var tiles_url = 'http://a.tiles.mapbox.com/v3/ericvanzanten.map-3ofkoxuh.jsonp';
        wax.tilejson(tiles_url, function(tilejson){
            var tiles = {
                tilejson: tilejson.tilejson,
                tiles: tilejson.tiles
            }
            map = L.map('map', {attributionControl: false});
            map.addLayer(new wax.leaf.connector(tiles));
            map.fitBounds([[41.644286009999995, -87.94010087999999], [42.023134979999995, -87.52366115999999]]);
            var attribution = new L.Control.Attribution();
            attribution.addAttribution("Geocoding data &copy; 2013 <a href='http://open.mapquestapi.com'>MapQuest, Inc.</a> | ");
            attribution.addAttribution("Tiles from <a href='http://mapbox.com/about/maps/'>MapBox</a> | ");
            attribution.addAttribution("Map data © <a href='http://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA.</a>");
            map.addControl(attribution);
        })
    })
})()
