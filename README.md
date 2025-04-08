# GeoDjango

## Frequently Used SQL Commands

### Verifying LineString

```sql
WITH
    start_node AS (
        SELECT "source" AS node_id 
        FROM orwn_track_noded
        ORDER BY the_geom <-> (SELECT geom FROM orwn_station WHERE id = 1) 
        LIMIT 1
    ),
    end_node AS (
        SELECT "target" AS node_id 
        FROM orwn_track_noded
        ORDER BY the_geom <-> (SELECT geom FROM orwn_station WHERE id = 2) 
        LIMIT 1
    ),
    route_edges AS (
        SELECT original.geom AS geom
        FROM pgr_dijkstra(
            'SELECT id,
                    old_id,
                    source,
                    target,
                    ST_Length(geom) AS cost
            FROM orwn_track_noded',
            (SELECT node_id FROM start_node), 
            (SELECT node_id FROM end_node),
            FALSE
        ) AS route
        JOIN orwn_track_noded AS edges ON route.edge = edges.id
        JOIN orwn_track AS original ON original.id = edges.old_id
    ),
    route_geom as (
        SELECT ST_LineMerge(ST_Collect(geom)) AS geom
        FROM route_edges
    )
select ST_AsText(geom) from route_geom
```

### Creating Noded Table and Topology

```sql
SELECT * from pgr_nodeNetwork('orwn_track', 0.0000045, 'id', 'geom');
SELECT pgr_createTopology('orwn_track_noded', 0.0000045, 'geom');
```