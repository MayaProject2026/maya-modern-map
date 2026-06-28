# Scripts

This folder contains data processing scripts for the Maya Modern Map project.

## Files

- `convert_sites.py` — Converts the EAAMS shapefile to GeoJSON format for use by the web application.

## Requirements

Python 3.9 or later, with the following packages:

- geopandas
- shapely
- fiona

Install with:
pip install geopandas shapely fiona
## Usage

Place the EAAMS shapefile (.shp, .dbf, .shx, .prj) in the `data/raw/` directory, then run:
python scripts/convert_sites.py
Output is written to `data/maya_sites.geojson`.
