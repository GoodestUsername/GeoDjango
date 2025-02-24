import json

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OrwnStation


@api_view(["GET"])
def closest_station(request):
    if request.method != 'GET':
        return Response(status=404)

    try:
        lon = request.GET.get('lon')
        lat = request.GET.get('lat')

        if lon is None or lat is None:
            return Response({"error": "Missing 'lon' or 'lat' parameter"}, status=400)

        try:
            lon = float(lon)
            lat = float(lat)
        except ValueError:
            return Response({"error": "Invalid 'lon' or 'lat' value"}, status=400)

        user_location = Point(lon, lat, srid=4269)

        nearest_station = (
            OrwnStation.objects.annotate(distance=Distance('shape', user_location))
            .order_by('distance')
            .first()
        )

        if not nearest_station:
            return Response({"error": "No station found"}, status=404)

        serialized = serialize("geojson", [nearest_station], geometry_field="shape", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Invalid coordinates"}, status=400)
