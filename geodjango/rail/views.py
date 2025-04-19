import json
from typing import Type
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point, GEOSGeometry
from django.core.serializers import serialize
from django.db import connection
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
    OrwnTrackNoded,
)

DEFAULT_LIMIT = 30


def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# region closest_fn

# region helpers


def parse_query_params_closest(request):
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
            distance=Distance("geom", user_location)
        ).order_by("distance")[:limit]

        if not queried:
            return Response({"error": "None found"}, status=404)

        serialized = serialize("geojson", queried, geometry_field="geom", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Invalid coordinates"}, status=400)


# endregion helpers


# region concrete
@api_view(["GET"])
def closest_crossings(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnCrossing)


@api_view(["GET"])
def closest_junctions(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnJunction)


@api_view(["GET"])
def closest_marker_posts(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnMarkerPost)


@api_view(["GET"])
def closest_stations(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnStation)


@api_view(["GET"])
def closest_structure_lines(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnStructureLine)


@api_view(["GET"])
def closest_structure_points(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnStructurePoint)


@api_view(["GET"])
def closest_tracks(request):
    args = parse_query_params_closest(request)
    if not isinstance(args, dict):
        return args

    return get_closest(args["lat"], args["lon"], args["limit"], OrwnTrack)


# endregion concrete

# endregion closest_fn


# region get all
@api_view(["GET"])
def stations(_):
    try:
        queried = OrwnStation.objects.all()

        if not queried:
            return Response({"error": "None found"}, status=404)

        serialized = serialize("geojson", queried, geometry_field="geom", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Internal Server Error"}, status=400)

@api_view(["GET"])
def tracks(_):
    try:
        queried = OrwnTrack.objects.all()

        if not queried:
            return Response({"error": "None found"}, status=404)

        serialized = serialize("geojson", queried, geometry_field="geom", srid=4269)

        return Response(json.loads(serialized), status=200)

    except (TypeError, ValueError):
        return Response({"error": "Internal Server Error"}, status=400)

# endregion get all

# region x between two points

# region helpers


def parse_query_params_two_points_srid(request):
    if request.method != "GET":
        return Response(status=404)

    try:
        from_lon = json.loads(request.GET.get("from_lon"))
        to_lon = json.loads(request.GET.get("to_lon"))

        srid = request.GET.get("srid")

        if from_lon is None or to_lon is None or srid is None:
            return Response({"error": "Missing a parameter"}, status=400)

        try:
            from_lon = float(from_lon)
            to_lon = float(to_lon)

            srid = int(srid)

            return {
                "from_lon": from_lon,
                "to_lon": to_lon,
                "srid": srid,
            }
        except ValueError:
            return Response({"error": "Invalid type value"}, status=400)

    except (TypeError, ValueError):
        return Response({"error": "Bad params"}, status=400)


def get_inbetween_points(
    srid: int,
    from_lon: float,
    to_lon: float,
    model: Type[Model],
):
    try:
        table_name = model._meta.db_table

        min_x = min(from_lon, to_lon)
        max_x = max(from_lon, to_lon)

        result = model.objects.raw(
            f"""
                SELECT *
                FROM {table_name}
                WHERE ST_Intersects(
                    {table_name}.geom,
                    ST_MakeEnvelope(
                        {min_x},
                        (SELECT MIN(ST_YMin({table_name}.geom)) FROM {table_name}),
                        {max_x},
                        (SELECT MAX(ST_YMax({table_name}.geom)) FROM {table_name}),
                        {srid}
                    )
                )"""
        )

        serialized = serialize("geojson", result, geometry_field="geom", srid=srid)

        return Response(serialized, status=200)
    except Exception as e:
        print(f"exception: {e}")
        return Response({"error": "Internal Server Error"}, status=500)


# endregion helpers


# region concrete
@api_view(["GET"])
def crossings_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnCrossing,
    )


@api_view(["GET"])
def junctions_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnJunction,
    )


@api_view(["GET"])
def marker_posts_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnMarkerPost,
    )


@api_view(["GET"])
def stations_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnStation,
    )


@api_view(["GET"])
def structure_lines_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnStructureLine,
    )


@api_view(["GET"])
def structure_points_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnStructurePoint,
    )


@api_view(["GET"])
def tracks_inbetween_points(request):
    args = parse_query_params_two_points_srid(request)
    if not isinstance(args, dict):
        return args

    return get_inbetween_points(
        args["srid"],
        args["from_lon"],
        args["to_lon"],
        OrwnTrack,
    )


# endregion concrete

# endregion x between two points

# region routing


@api_view(["GET"])
def station_route_for_track(request):
    from_station_id = int(request.GET.get("from_station_id"))
    to_station_id = int(request.GET.get("to_station_id"))

    try:
        station_table_name = OrwnStation._meta.db_table
        track_table_name = OrwnTrack._meta.db_table
        track_noded_table_name = OrwnTrackNoded._meta.db_table

        with (connection.cursor() as cursor):
            cursor.execute(
                f"""
                    WITH 
                        start_node AS (
                            SELECT "source" AS node_id 
                            FROM {track_noded_table_name}
                            ORDER BY geom <-> (SELECT geom FROM {station_table_name} WHERE id = {from_station_id}) 
                            LIMIT 1
                        ),
                        end_node AS (
                            SELECT "target" AS node_id 
                            FROM {track_noded_table_name}
                            ORDER BY geom <-> (SELECT geom FROM {station_table_name} WHERE id = {to_station_id}) 
                            LIMIT 1
                        ),    
                        route AS (
                            SELECT 
                                row_to_json(route.*) as route_info,
                                row_to_json(edges.*) as edges,
                                row_to_json(original.*) as orwn_track,
                                row_to_json(station.*) as orwn_station
                            FROM pgr_dijkstra(
                                    'SELECT id, old_id, source, target, ST_Length(geom) AS cost
                                    FROM {track_noded_table_name}',
                                    (SELECT node_id FROM start_node), 
                                    (SELECT node_id FROM end_node),
                                    FALSE
                            ) AS route
                            LEFT JOIN {track_noded_table_name} AS edges
                                ON route.edge = edges.id
                            LEFT JOIN {track_table_name} AS original
                                ON original.id = edges.old_id
                            LEFT JOIN {station_table_name} AS station
                                ON  ST_Intersects(station.geom, edges.geom)
                            ORDER BY seq ASC, ST_LineLocatePoint(edges.geom, station.geom) asc
                        )
                    select 
                        json_agg(route_info) as routing, 
                        json_agg(edges) as edge, 
                        json_agg(orwn_track) as orwn_track, 
                        json_agg(orwn_station) as orwn_station
                    from route
                """,
            )
            result = dict_fetch_all(cursor)
            if len(result) == 1:
                return Response(result[0], status=200)
            return Response(status=404)
        # return row

        # serialized = serialize("geojson", result, geometry_field="geom", srid=srid)

        # return Response(serialized, status=200)
    except Exception as e:
        print(f"exception: {e}")
        return Response({"error": "Internal Server Error"}, status=500)


# endregion routing
