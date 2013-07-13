from django.contrib.gis import admin
from illuminator.models import Ward, TifDistricts, PinsMaster

class WardAdmin(admin.GeoModelAdmin):
    search_fields = ['ward', 'alderman']
    list_display = ('ward', 'alderman')
admin.site.register(Ward, WardAdmin)

class TifAdmin(admin.GeoModelAdmin):
    pass
admin.site.register(TifDistricts, TifAdmin)

class PinsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PinsMaster, PinsAdmin)
