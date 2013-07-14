from __future__ import unicode_literals

from django.contrib.gis.db import models

class Ward(models.Model):
    perimeter = models.FloatField()
    ward = models.CharField(max_length=4)
    alderman = models.CharField(max_length=60)
    ward_phone = models.CharField(max_length=12)
    hall_phone = models.CharField(max_length=12)
    hall_office = models.CharField(max_length=45)
    address = models.CharField(max_length=39)
    edit_date1 = models.CharField(max_length=10)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=3435)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.ward

class TifDistrict(models.Model):
    name = models.CharField(max_length=50)
    ind = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    use = models.CharField(max_length=50)
    repealed_date = models.DateTimeField(null=True, blank=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    ref_number = models.CharField(max_length=7, null=True)
    revenue2010 = models.CharField(max_length=15, null=True)
    revenue2011 = models.CharField(max_length=15, null=True)
    geom = models.MultiPolygonField(srid=3435)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Overlap(models.Model):
    ward = models.ForeignKey(Ward)
    tif = models.ForeignKey(TifDistrict)
    overlap = models.MultiPolygonField(srid=3435)
    
    def __unicode__(self):
        return 'TIF %s area overlapping Ward %s' % (self.tif.ref_number, self.ward.ward)

