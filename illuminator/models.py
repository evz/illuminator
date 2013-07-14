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

class PinsMaster(models.Model):
    pin = models.CharField(max_length=30, blank=True)
    taxcode = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    amt_billed = models.TextField(blank=True)
    year = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return self.pin

    class Meta:
        db_table = 'pins_master'

class PropertyValues(models.Model):
    pin = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    township = models.CharField(max_length=50, blank=True)
    assessment_tax_year = models.CharField(max_length=200, blank=True)
    est_value = models.CharField(max_length=200, blank=True)
    assessed_value = models.CharField(max_length=200, blank=True)
    lotsize = models.CharField(max_length=200, blank=True)
    bldg_size = models.CharField(max_length=200, blank=True)
    property_class = models.CharField(max_length=200, blank=True)
    bldg_age = models.CharField(max_length=10, blank=True)
    tax_rate_year = models.CharField(max_length=200, blank=True)
    tax_code_year = models.CharField(max_length=200, blank=True)
    taxcode = models.CharField(max_length=10, blank=True)
    mailing_tax_year = models.CharField(max_length=200, blank=True)
    mailing_name = models.CharField(max_length=100, blank=True)
    mailing_address = models.CharField(max_length=250, blank=True)
    mailing_city_state_zip = models.CharField(max_length=250, blank=True)
    tax_bill_2012 = models.CharField(max_length=200, blank=True)
    tax_bill_2011 = models.CharField(max_length=200, blank=True)
    tax_bill_2010 = models.CharField(max_length=200, blank=True)
    tax_bill_2009 = models.CharField(max_length=200, blank=True)
    tax_bill_2008 = models.CharField(max_length=200, blank=True)
    tax_bill_2007 = models.CharField(max_length=200, blank=True)
    tax_bill_2006 = models.CharField(max_length=200, blank=True)
    tax_rate = models.CharField(max_length=10, blank=True)
    sent_pin = models.CharField(max_length=20, blank=True)
    bldg_gid = models.IntegerField(null=True, blank=True)
    est_value_calc = models.TextField(blank=True) # This field type is a guess.
    str_num = models.CharField(max_length=10, blank=True)
    str_dir = models.CharField(max_length=10, blank=True)
    str_name = models.CharField(max_length=75, blank=True)
    str_typ = models.CharField(max_length=50, blank=True)
    full_address = models.CharField(max_length=200, blank=True)
    the_geom = models.PointField(srid=3435, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'property_values'

class SbifGrantAgreements(models.Model):
    company = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    tif = models.ForeignKey('TifDistricts', null=True, blank=True)
    tif_name = models.CharField(max_length=150, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    actual_cost = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    actual_grant_work = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    work_items = models.TextField(blank=True)
    id = models.IntegerField(primary_key=True)
    bldg_gid = models.IntegerField(null=True, blank=True)
    str_num = models.CharField(max_length=50, blank=True)
    str_dir = models.CharField(max_length=10, blank=True)
    str_name = models.CharField(max_length=75, blank=True)
    the_geom = models.PointField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'sbif_grant_agreements'

class Taxcode(models.Model):
    entity = models.CharField(max_length=100, blank=True)
    taxcode = models.CharField(max_length=10, blank=True)
    agency = models.CharField(max_length=25, blank=True)
    tax_rate = models.CharField(max_length=50, blank=True)
    percent = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=50, blank=True)
    tif = models.ForeignKey('TifStatusEligibility', null=True, blank=True)
    class Meta:
        db_table = 'taxcode'

class TifDistricts(models.Model):
    gid = models.IntegerField(primary_key=True)
    tif_name = models.CharField(max_length=50, blank=True)
    ind = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=15, blank=True)
    use = models.CharField(max_length=50, blank=True)
    repealed_d = models.CharField(max_length=10, blank=True)
    approval_d = models.CharField(max_length=10, blank=True)
    expiration = models.CharField(max_length=10, blank=True)
    the_geom = models.MultiPolygonField(srid=3435, null=True, blank=True)
    tif_id = models.CharField(max_length=5, unique=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.tif_name

    class Meta:
        db_table = 'tif_districts'

class TifDistrict(models.Model):
    name = models.CharField(max_length=50)
    ind = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    use = models.CharField(max_length=50)
    repealed_date = models.DateTimeField(null=True, blank=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    ref_number = models.CharField(max_length=7, null=True)
    geom = models.MultiPolygonField(srid=3435)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class TifProjectionReports(models.Model):
    tif = models.ForeignKey(TifDistricts, null=True, blank=True)
    tif_name = models.CharField(max_length=100, blank=True)
    reporting_category = models.CharField(max_length=100, blank=True)
    item = models.TextField(blank=True)
    year = models.IntegerField(null=True, blank=True)
    amount = models.TextField(blank=True) # This field type is a guess.
    end_date = models.DateField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'tif_projection_reports'

class TifStatusEligibility(models.Model):
    status = models.CharField(max_length=25, blank=True)
    tif_id = models.CharField(max_length=10, unique=True, blank=True)
    tif_name = models.CharField(max_length=100, blank=True)
    designation_date = models.DateField(null=True, blank=True)
    designation_year = models.SmallIntegerField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    final_year = models.SmallIntegerField(null=True, blank=True)
    blighting = models.NullBooleanField(null=True, blank=True)
    conservation = models.NullBooleanField(null=True, blank=True)
    redevelopment_plan = models.TextField(blank=True)
    class Meta:
        db_table = 'tif_status_eligibility'

class Overlap(models.Model):
    ward = models.ForeignKey(Ward)
    tif = models.ForeignKey(TifDistricts)
    revenue2010 = models.CharField(max_length=15, null=True)
    revenue2011 = models.CharField(max_length=15, null=True)
    overlap = models.MultiPolygonField(srid=3435)
    
    def __unicode__(self):
        return 'TIF %s area overlapping Ward %s' % (self.tif.tif_id, self.ward.ward)
