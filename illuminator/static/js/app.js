(function(){
    var map;
    $(document).ready(function(){
        var tiles_url = 'http://a.tiles.mapbox.com/v3/ericvanzanten.map-3ofkoxuh.jsonp';
        wax.tilejson(tiles_url, function(tilejson){
            var tiles = {
                tilejson: tilejson.tilejson,
                tiles: tilejson.tiles
            }
            map = L.map('map', {attributionControl: false, scrollWheelZoom: false});
            map.addLayer(new wax.leaf.connector(tiles));
            map.fitBounds([[41.644286009999995, -87.94010087999999], [42.023134979999995, -87.52366115999999]]);
            var attribution = new L.Control.Attribution();
            attribution.addAttribution("Geocoding data &copy; 2013 <a href='http://open.mapquestapi.com'>MapQuest, Inc.</a> | ");
            attribution.addAttribution("Tiles from <a href='http://mapbox.com/about/maps/'>MapBox</a> | ");
            attribution.addAttribution("Map data © <a href='http://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA.</a>");
            map.addControl(attribution);
        });
        $('.search').on('click',function(e){
            e.preventDefault();
            $('#refine').empty()
            var query = $(this).prev().val() + ' Chicago, IL';
            var bbox = "42.023134979999995,-87.52366115999999,41.644286009999995,-87.94010087999999";
            var params = {
                key: 'Fmjtd|luub2d0rn1,rw=o5-9u2ggw',
                location: query,
                boundingBox: bbox
            }
            $.ajax({
                url:'http://open.mapquestapi.com/geocoding/v1/address',
                data: params,
                dataType: 'jsonp',
                success: handle_geocode
            });
        });
    });
    function handle_geocode(data){
        var locations = data.results[0].locations;
        if (locations.length == 1) {
            var latlng = [locations[0].latLng.lat, locations[0].latLng.lng];
            map.setView(latlng, 17);
            L.marker(latlng).addTo(map);
        } else if (locations.length > 1) {
            var tpl = new EJS({url: 'static/js/views/searchRefine.ejs'});
            $('#refine').append(tpl.render({locations:locations}));
            var width = $('.map-search input').width() + $('.map-search button').width();
            $('#refine').width(width);
            $('.refine-search').on('click', function(e){
                e.preventDefault();
                var data = $(this).parent().data('latlng').split(',');
                var latlng = [parseFloat(data[0]), parseFloat(data[1])];
                map.setView(latlng, 17);
                L.marker(latlng).addTo(map);
            });
        } else {
            $('#refine').append("<p>Your search didn't return any results.</p>");
        }
    }
})()
