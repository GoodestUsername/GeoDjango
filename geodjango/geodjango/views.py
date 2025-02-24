from django.http import JsonResponse
from django.db import connection
from django.core.serializers import serialize

from world.models.public import OrwnStation

def geo_data(request):
    #result = City.objects.raw("SELECT id, name, %s as point from orwn_station" % (connection.ops.select %  "point"))
    result = OrwnStation.objects.raw("SELECT * from orwn_station")
    print("RESULT", len(result), result)
    station = result[0]
    print("FIRST STATION", station)
    station = dict(name=station.stenname)#, shape=station.shape)
    geojson = serialize("geojson", result, geometry_field="shape", fields=["stenname"])
    print('geojson', geojson)
    return JsonResponse({'data': geojson})
    #return JsonResponse({'data': 'geo data', 'result': station})
