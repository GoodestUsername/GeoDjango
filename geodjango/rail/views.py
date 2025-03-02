import json
from typing import Type
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Model
from .models import (
    OrwnStation,
    OrwnCrossing,
    OrwnJunction,
    OrwnMarkerPost,
    OrwnStructureLine,
    OrwnStructurePoint,
    OrwnTrack,
)

DEFAULT_LIMIT = 30


def parse_query_params(request):
    if request.method != "GET":
        return Response(status=404)

    try:
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        limit = request.GET.get("limit") or DEFAULT_LIMIT

        if lat is None or lon is None:
            return Response({"error": "Missing 'lon' or 'lat' parameter"}, status=400)

        try:
            lat = float(lat)
            lon = float(lon)
            limit = float(limit)
        except ValueError:
            return Response(
                {"error": "Invalid 'lat' or 'lon' or 'limit' value"}, status=400
            )

        return {"lat": lat, "lon": lon, "limit": limit}

    except (TypeError, ValueError):
        return Response({"error": "Invalid coordinates or limit"}, status=400)


def get_closest(lat, lon, limit, model: Type[Model]):
    try:
        user_location = Point(lat, lon, srid=4269)

        queried = model.objects.annotate(
            distance=Distance("shape", user_location)
        ).order_by("distance")[:limit]

        if not queried:
            return Response({"error": "None found"}, status=404)

        serialized = serialize("geojson", queried, geometry_field="shape", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Invalid coordinates"}, status=400)


@api_view(["GET"])
def closest_crossings(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnCrossing)
    else:
        return args


@api_view(["GET"])
def closest_junctions(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnJunction)
    else:
        return args


@api_view(["GET"])
def closest_marker_posts(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnMarkerPost)
    else:
        return args


@api_view(["GET"])
def closest_stations(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnStation)
    else:
        return args


@api_view(["GET"])
def closest_structure_lines(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnStructureLine)
    else:
        return args


@api_view(["GET"])
def closest_structure_points(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnStructurePoint)
    else:
        return args


@api_view(["GET"])
def closest_tracks(request):
    args = parse_query_params(request)
    if isinstance(args, dict):
        return get_closest(args["lat"], args["lon"], args["limit"], OrwnTrack)
    else:
        return args


@api_view(["GET"])
def stations(request):
    try:
        queried = OrwnStation.objects.all()

        if not queried:
            return Response({"error": "None found"}, status=404)

        serialized = serialize("geojson", queried, geometry_field="shape", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Invalid coordinates"}, status=400)


@api_view(["GET"])
def tracks_inbetween_points(request):
    if request.method != "GET":
        return Response(status=404)

    try:
        from_lat = json.loads(request.GET.get("from_lat"))
        from_lon = json.loads(request.GET.get("from_lon"))

        to_lat = json.loads(request.GET.get("to_lat"))
        to_lon = json.loads(request.GET.get("to_lon"))

        srid = request.GET.get("srid")

        if from_lat is None or from_lon is None or to_lat is None or to_lon is None or srid is None:
            return Response({"error": "Missing a parameter"}, status=400)

        try:
            from_lat = float(from_lat)
            from_lon = float(from_lon)

            to_lat = float(to_lat)
            to_lon = float(to_lon)

            srid = int(srid)
        except ValueError:
            return Response(
                {"error": "Invalid type value"}, status=400
            )

        try:
            result = OrwnTrack.objects.raw(
                f"WITH bbox AS ("
                    f"SELECT ST_SetSRID(ST_Envelope(ST_Collect(shape)), {srid}) AS shape "
                    f"FROM (VALUES "
                        f"(ST_SetSRID(ST_MakePoint({from_lon}, {from_lat}), {srid})),"
                        f"(ST_SetSRID(ST_MakePoint({to_lon}, {to_lat}), {srid}))"
                f") AS points(shape)) "
                f"SELECT * "
                f"FROM orwn_track, bbox "
                f"WHERE ST_Intersects(orwn_track.shape, bbox.shape);"
            )

            serialized = serialize("geojson", result, geometry_field="shape", srid=4269)

            return Response(serialized, status=200)
        except Exception as e:
            print(f'exception: {e}')
            return Response({"error": "Internal Server Error"}, status=500)

    except (TypeError, ValueError):
        return Response({"error": "Invalid from and to points."}, status=400)
