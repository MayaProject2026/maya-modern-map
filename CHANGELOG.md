# Changelog

A log of significant changes and progress on the Maya Modern Map project.

## 2026-06-28

### Core map implementation

- Replaced the placeholder index.html with a working Leaflet.js implementation
- Map loads Leaflet v1.9.4 from the unpkg CDN with subresource integrity checks
- Default view centred on the Maya region at coordinates (16.5, -89.5), zoom level 6
- OpenStreetMap configured as the default basemap
- Mobile viewport meta tag added to support touch interaction
- Full-viewport responsive layout with loading indicator

### Foundation and infrastructure

- Created GitHub repository at github.com/MayaProject2026/maya-modern-map
- Configured MIT licence and .gitignore for Python and shapefile artifacts
- Set up project README with full description, technology stack, and architecture overview
- Enabled GitHub Pages deployment from the main branch
- Live site now available at https://mayaproject2026.github.io/maya-modern-map/

### Repository structure

- Created scripts/ folder with documentation for the data conversion pipeline
- Created data/ folder with documentation describing the EAAMS source data and CRS conventions

### Data conversion pipeline

- Implemented scripts/convert_sites.py to convert the EAAMS shapefile to GeoJSON
- Script handles CRS reprojection to WGS84, filtering of unnamed records, attribute normalisation, and UTF-8 encoding of non-ASCII site names
- Output written to data/maya_sites.geojson as an RFC 7946 compliant FeatureCollection
