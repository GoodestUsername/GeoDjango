"""
URL configuration for geodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rail import views

urlpatterns = [
    # path("geo_data", views.geo_data),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('stations/', views.stations),
    path('closest_crossings/', views.closest_crossings),
    path('closest_junctions/', views.closest_junctions),
    path('closest_marker_posts/', views.closest_marker_posts),
    path('closest_stations/', views.closest_stations),
    path('closest_structure_lines/', views.closest_structure_lines),
    path('closest_structure_points/', views.closest_structure_points),
    path('closest_tracks/', views.closest_tracks),
    path('crossings_inbetween_points/', views.crossings_inbetween_points),
    path('junctions_inbetween_points/', views.junctions_inbetween_points),
    path('marker_posts_inbetween_points/', views.marker_posts_inbetween_points),
    path('stations_inbetween_points/', views.stations_inbetween_points),
    path('structure_lines_inbetween_points/', views.structure_lines_inbetween_points),
    path('structure_points_inbetween_points/', views.structure_points_inbetween_points),
    path('structure_points_inbetween_points/', views.structure_points_inbetween_points),
    path('tracks_inbetween_points/', views.tracks_inbetween_points),
    path('station_route_for_track/', views.station_route_for_track),
]
