"""
This script can be added to your Django project to modify GDAL settings at runtime.
Run it at the beginning of your Django app's initialization.
"""
from django.contrib.gis.gdal import gdal_library_path
from django.contrib.gis.geos import geos_library_path
import os
import ctypes
import sys
from pathlib import Path


def set_gdal_paths():
    """
    Fix GDAL paths for Linux container environment.
    This will override any hardcoded Windows paths.
    """
    # Get environment variables if set
    gdal_path = os.environ.get('GDAL_LIBRARY_PATH', '/usr/lib/x86_64-linux-gnu/libgdal.so')
    geos_path = os.environ.get('GEOS_LIBRARY_PATH', '/usr/lib/x86_64-linux-gnu/libgeos_c.so')

    # Check if we're in a container (Linux environment)
    if os.name == 'posix' and os.environ.get('IN_DOCKER'):
        try:
            # Try to load the libraries to verify they exist
            ctypes.CDLL(gdal_path)
            ctypes.CDLL(geos_path)

            # Set the paths in Django's internals
            os.environ['GDAL_LIBRARY_PATH'] = gdal_path
            os.environ['GEOS_LIBRARY_PATH'] = geos_path

            print(f"GDAL path set to: {gdal_path}")
            print(f"GEOS path set to: {geos_path}")
        except Exception as e:
            print(f"Error setting GDAL/GEOS paths: {e}")
    else:
        print("Not in Docker container or not a Linux environment. Using default paths.")


# Run automatically when imported
set_gdal_paths()
