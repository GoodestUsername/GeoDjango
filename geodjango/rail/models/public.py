from django.contrib.gis.db import models


class OrwnCrossing(models.Model):
    id = models.AutoField(primary_key=True)
    ogf_id = models.FloatField(blank=True, null=True, default=0)
    nid = models.CharField(max_length=32, blank=True, null=True)
    crossingid = models.CharField(max_length=32, blank=True, null=True)
    levelcross = models.CharField(max_length=15, blank=True, null=True)
    crossintyp = models.CharField(max_length=25, blank=True, null=True)
    warningsys = models.CharField(max_length=20, blank=True, null=True)
    roadclass = models.CharField(max_length=20, blank=True, null=True)
    crosstypnm = models.CharField(max_length=100, blank=True, null=True)
    routenumbe = models.CharField(max_length=10, blank=True, null=True)
    crosacces = models.CharField(max_length=7, blank=True, null=True)
    tcid = models.IntegerField(blank=True, null=True, default=0)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1dist = models.FloatField(blank=True, null=True, default=0)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub1disty = models.CharField(max_length=15, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2dist = models.FloatField(blank=True, null=True, default=0)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub2disty = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True, default=0)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_crossing"


class OrwnJunction(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True, default=0)
    nid = models.CharField(max_length=32, blank=True, null=True)
    bndytrind = models.CharField(max_length=5, blank=True, null=True)
    subdlimind = models.CharField(max_length=5, blank=True, null=True)
    trajunctyp = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True, default=0)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_junction"


class OrwnMarkerPost(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True, default=0)
    nid = models.CharField(max_length=32, blank=True, null=True)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1dist = models.FloatField(blank=True, null=True, default=0)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub1disty = models.CharField(max_length=15, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2dist = models.FloatField(blank=True, null=True, default=0)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub2disty = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True, default=0)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_marker_post"


class OrwnStation(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True, default=0)
    nid = models.CharField(max_length=32, blank=True, null=True)
    stenname = models.CharField(max_length=100, blank=True, null=True)
    stfrname = models.CharField(max_length=100, blank=True, null=True)
    stntype = models.CharField(max_length=20, blank=True, null=True)
    numplatefr = models.SmallIntegerField(blank=True, null=True, default=0)
    stnusr1ena = models.CharField(max_length=100, blank=True, null=True)
    stnusr1fna = models.CharField(max_length=100, blank=True, null=True)
    stnusr1rmk = models.CharField(max_length=10, blank=True, null=True)
    stnusr2ena = models.CharField(max_length=100, blank=True, null=True)
    stnusr2fna = models.CharField(max_length=100, blank=True, null=True)
    stnusr2rmk = models.CharField(max_length=10, blank=True, null=True)
    stnusr3ena = models.CharField(max_length=100, blank=True, null=True)
    stnusr3fna = models.CharField(max_length=100, blank=True, null=True)
    stnusr3rmk = models.CharField(max_length=10, blank=True, null=True)
    stnusr4ena = models.CharField(max_length=100, blank=True, null=True)
    stnusr4fna = models.CharField(max_length=100, blank=True, null=True)
    stnusr4rmk = models.CharField(max_length=10, blank=True, null=True)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1dist = models.FloatField(blank=True, null=True, default=0)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub1disty = models.CharField(max_length=15, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2dist = models.FloatField(blank=True, null=True, default=0)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub2disty = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True, default=0)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_station"


class OrwnStructureLine(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True)
    nid = models.CharField(max_length=32, blank=True, null=True)
    strucid = models.CharField(max_length=32, blank=True, null=True)
    struenname = models.CharField(max_length=100, blank=True, null=True)
    strufrname = models.CharField(max_length=100, blank=True, null=True)
    structype = models.CharField(max_length=15, blank=True, null=True)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1dist = models.FloatField(blank=True, null=True)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub1disty = models.CharField(max_length=15, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2dist = models.FloatField(blank=True, null=True)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub2disty = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)
    geom_length = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_structure_line"


class OrwnStructurePoint(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True)
    nid = models.CharField(max_length=32, blank=True, null=True)
    strucid = models.CharField(max_length=32, blank=True, null=True)
    structype = models.CharField(max_length=15, blank=True, null=True)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1dist = models.FloatField(blank=True, null=True)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub1disty = models.CharField(max_length=15, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2dist = models.FloatField(blank=True, null=True)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    sub2disty = models.CharField(max_length=15, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_structure_point"


class OrwnTrack(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.GeometryField(srid=4269, blank=True, null=True)
    ogf_id = models.FloatField(blank=True, null=True)
    tracknid = models.CharField(max_length=32, blank=True, null=True)
    tracksegid = models.CharField(max_length=32, blank=True, null=True)
    trackname = models.CharField(max_length=100, blank=True, null=True)
    trackclass = models.CharField(max_length=20, blank=True, null=True)
    regulator = models.CharField(max_length=10, blank=True, null=True)
    transptype = models.CharField(max_length=10, blank=True, null=True)
    usetype = models.CharField(max_length=25, blank=True, null=True)
    gauge = models.CharField(max_length=10, blank=True, null=True)
    numtracks = models.SmallIntegerField(blank=True, null=True)
    electric = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    speedfreit = models.SmallIntegerField(blank=True, null=True)
    speedpasse = models.SmallIntegerField(blank=True, null=True)
    unitofspee = models.CharField(max_length=20, blank=True, null=True)
    sourceid = models.CharField(max_length=50, blank=True, null=True)
    operatoena = models.CharField(max_length=100, blank=True, null=True)
    operatofna = models.CharField(max_length=100, blank=True, null=True)
    operatormk = models.CharField(max_length=10, blank=True, null=True)
    opsubstart = models.FloatField(blank=True, null=True)
    opsubend = models.FloatField(blank=True, null=True)
    opsubudis = models.CharField(max_length=9, blank=True, null=True)
    ownerena = models.CharField(max_length=100, blank=True, null=True)
    ownerfna = models.CharField(max_length=100, blank=True, null=True)
    trkusr1ena = models.CharField(max_length=100, blank=True, null=True)
    trkusr1fna = models.CharField(max_length=100, blank=True, null=True)
    trkusr1rmk = models.CharField(max_length=10, blank=True, null=True)
    trkusr2ena = models.CharField(max_length=100, blank=True, null=True)
    trkusr2fna = models.CharField(max_length=100, blank=True, null=True)
    trkusr2rmk = models.CharField(max_length=10, blank=True, null=True)
    trkusr3ena = models.CharField(max_length=100, blank=True, null=True)
    trkusr3fna = models.CharField(max_length=100, blank=True, null=True)
    trkusr3rmk = models.CharField(max_length=10, blank=True, null=True)
    trkusr4ena = models.CharField(max_length=100, blank=True, null=True)
    trkusr4fna = models.CharField(max_length=100, blank=True, null=True)
    trkusr4rmk = models.CharField(max_length=10, blank=True, null=True)
    subdi1nid = models.CharField(max_length=32, blank=True, null=True)
    subdi1name = models.CharField(max_length=100, blank=True, null=True)
    subd1start = models.FloatField(blank=True, null=True)
    subd1end = models.FloatField(blank=True, null=True)
    sub1unitdi = models.CharField(max_length=9, blank=True, null=True)
    subdi2nid = models.CharField(max_length=32, blank=True, null=True)
    subdi2name = models.CharField(max_length=100, blank=True, null=True)
    subd2start = models.FloatField(blank=True, null=True)
    subd2end = models.FloatField(blank=True, null=True)
    sub2unitdi = models.CharField(max_length=9, blank=True, null=True)
    adminarea = models.CharField(max_length=7, blank=True, null=True)
    specvers = models.CharField(max_length=5, blank=True, null=True)
    securclass = models.CharField(max_length=12, blank=True, null=True)
    geocredate = models.CharField(max_length=8, blank=True, null=True)
    georevdate = models.CharField(max_length=8, blank=True, null=True)
    geoacqtech = models.CharField(max_length=25, blank=True, null=True)
    geoaccura = models.SmallIntegerField(blank=True, null=True)
    geoprovide = models.CharField(max_length=25, blank=True, null=True)
    attcredate = models.CharField(max_length=8, blank=True, null=True)
    attrevdate = models.CharField(max_length=8, blank=True, null=True)
    attacqtech = models.CharField(max_length=25, blank=True, null=True)
    attprovide = models.CharField(max_length=25, blank=True, null=True)
    effective_datetime = models.DateTimeField(blank=True, null=True)
    geom_length = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_track"


class OrwnTrackNoded(models.Model):
    id = models.BigAutoField(primary_key=True)
    old_id = models.IntegerField(blank=True, null=True)
    sub_id = models.IntegerField(blank=True, null=True)
    source = models.BigIntegerField(blank=True, null=True)
    target = models.BigIntegerField(blank=True, null=True)
    geom = models.LineStringField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_track_noded"


class OrwnTrackNodedVerticesPgr(models.Model):
    id = models.BigAutoField(primary_key=True)
    cnt = models.IntegerField(blank=True, null=True)
    chk = models.IntegerField(blank=True, null=True)
    ein = models.IntegerField(blank=True, null=True)
    eout = models.IntegerField(blank=True, null=True)
    the_geom = models.PointField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orwn_track_noded_vertices_pgr"
