"""
convert_sites.py

Converts the EAAMS (Electronic Atlas of Ancient Maya Sites) shapefile to a
GeoJSON FeatureCollection suitable for client-side rendering by Leaflet.js.

The EAAMS dataset is distributed by Walter Witschey and contains records for
approximately 6,341 Maya archaeological sites. This script filters out records
with missing or empty site names, normalises attribute fields, and writes a
single UTF-8 encoded GeoJSON file.

Usage:
    python scripts/convert_sites.py

Input:
    data/raw/EAAMS.shp (and companion .dbf, .shx, .prj files)

Output:
    data/maya_sites.geojson

Author: Blend Mameen
Project: CS5999 MSc Dissertation, University of St Andrews
Supervisor: Professor Lars Kotthoff
"""

import json
import sys
from pathlib import Path

import geopandas as gpd


# ── Paths ──────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
INPUT_SHAPEFILE = REPO_ROOT / "data" / "raw" / "EAAMS.shp"
OUTPUT_GEOJSON = REPO_ROOT / "data" / "maya_sites.geojson"


# ── Attribute mapping ──────────────────────────────────────────────────────
# Maps shapefile attribute field names to the cleaner property names used in
# the output GeoJSON. The EAAMS shapefile prefixes some fields with "BW"
# (for Bruce Witschey) and uses inconsistent casing.
FIELD_MAP = {
    "BWNAME": "name",
    "BWCOuntry": "country",
    "BWState": "state",
    "rank": "rank",
    "NOTES": "notes",
}


def main() -> None:
    """Run the full conversion pipeline."""

    if not INPUT_SHAPEFILE.exists():
        print(f"ERROR: Input shapefile not found at {INPUT_SHAPEFILE}")
        print("Place the EAAMS shapefile (and companions) in data/raw/")
        sys.exit(1)

    print(f"Reading shapefile from {INPUT_SHAPEFILE}...")
    gdf = gpd.read_file(INPUT_SHAPEFILE)
    print(f"  Loaded {len(gdf)} total records")
    print(f"  Coordinate reference system: {gdf.crs}")

    if gdf.crs is None or gdf.crs.to_epsg() != 4326:
        print("  Reprojecting to WGS84 (EPSG:4326)...")
        gdf = gdf.to_crs(epsg=4326)

    initial_count = len(gdf)
    gdf = gdf[gdf["BWNAME"].notna() & (gdf["BWNAME"].astype(str).str.strip() != "")]
    print(f"  Filtered to {len(gdf)} named sites (removed {initial_count - len(gdf)} unnamed records)")

    features = []
    for _, row in gdf.iterrows():
        properties = {}
        for shapefile_field, geojson_property in FIELD_MAP.items():
            value = row.get(shapefile_field)
            if value is None or (isinstance(value, float) and value != value):
                properties[geojson_property] = None
            else:
                properties[geojson_property] = value

        if properties.get("rank") is not None:
            try:
                properties["rank"] = int(properties["rank"])
            except (ValueError, TypeError):
                properties["rank"] = None

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row.geometry.x, row.geometry.y],
            },
            "properties": properties,
        }
        features.append(feature)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features,
    }

    OUTPUT_GEOJSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_GEOJSON, "w", encoding="utf-8") as f:
        json.dump(feature_collection, f, ensure_ascii=False, indent=2)

    file_size_kb = OUTPUT_GEOJSON.stat().st_size / 1024
    print(f"\nWrote {len(features)} features to {OUTPUT_GEOJSON}")
    print(f"  File size: {file_size_kb:.1f} KB")
    print("Conversion complete.")


if __name__ == "__main__":
    main()
