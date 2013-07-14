from django.contrib.gis import admin
from illuminator.models import Ward, TifDistrict, PinsMaster

class WardAdmin(admin.GeoModelAdmin):
    search_fields = ['ward', 'alderman']
    list_display = ('ward', 'alderman')
admin.site.register(Ward, WardAdmin)

class TifAdmin(admin.GeoModelAdmin):
    search_fields = ['name', 'ref_number']
    list_display = ('name', 'ref_number')
admin.site.register(TifDistrict, TifAdmin)

class PinsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PinsMaster, PinsAdmin)
