from django.contrib.gis import admin
from illuminator.models import Ward, TifDistrict, Overlap, TifProjectionReport
from illuminator.widgets import LeafletWidget

class WardAdmin(admin.GeoModelAdmin):
    search_fields = ['ward', 'alderman']
    list_display = ('ward', 'alderman')
    map_template = 'admin_map.html'
    widget = LeafletWidget
admin.site.register(Ward, WardAdmin)

class TifAdmin(admin.GeoModelAdmin):
    search_fields = ['name', 'ref_number']
    list_display = ('name', 'ref_number')
    map_template = 'admin_map.html'
    widget = LeafletWidget
admin.site.register(TifDistrict, TifAdmin)

class ProjAdmin(admin.ModelAdmin):
    pass
admin.site.register(TifProjectionReport, ProjAdmin)

class OverlapAdmin(admin.GeoModelAdmin):
    search_fields = ['tif__name', 'ward__ward']
    list_display = ('tif_name', 'ward_number',)

    map_template = 'admin_map.html'
    widget = LeafletWidget

    def tif_name(self, obj):
        return obj.tif.name

    def ward_number(self, obj):
        return obj.ward.ward
admin.site.register(Overlap, OverlapAdmin)
