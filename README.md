# Maya Modern Map

A modernised reimplementation of [mayamap.org](http://mayamap.org), built using Leaflet.js and GeoJSON with a fully client-side, statically hosted architecture.

**Live demo:** https://mayaproject2026.github.io/maya-modern-map/

## About

This project is part of an MSc Data Science dissertation at the University of St Andrews (CS5999), supervised by Professor Lars Kotthoff. It modernises the existing mayamap.org interactive web map of Maya archaeological sites by replacing its OpenLayers 2 / server-side raster tile architecture with a fully client-side implementation using Leaflet.js and GeoJSON.

The application provides an interactive map of around 5,200 named Maya archaeological sites drawn from the Electronic Atlas of Ancient Maya Sites (EAAMS) dataset compiled by archaeologist Walter Witschey.

## Features

The reimplemented system aims to deliver:

- Interactive map with multiple basemap options (OpenStreetMap, CartoDB, ESRI)
- Site name search with live filtering
- Filtering by archaeological rank and country
- Three visualisation modes: point markers, proportional bubbles, density heatmap
- Proximity analysis tool using the Haversine formula
- User geolocation feature
- Regional analytics dashboard
- Mobile-responsive layout

## Technology Stack

| Component | Technology |
|---|---|
| Map engine | Leaflet.js v1.9.4 |
| Marker clustering | Leaflet.markercluster |
| Heatmap rendering | Leaflet.heat |
| Charts | Chart.js |
| Data format | GeoJSON (RFC 7946) |
| Data conversion | Python 3 with GeoPandas |
| Hosting | GitHub Pages |

## Project Status

Active development. See CHANGELOG.md for progress.

## Repository Structure

maya-modern-map/
- index.html (main application)
- scripts/convert_sites.py (shapefile to GeoJSON conversion)
- data/maya_sites.geojson (converted site data)
- README.md
- CHANGELOG.md
- LICENSE

## Licence

MIT License. See LICENSE for details.

## Acknowledgements

EAAMS dataset compiled by Walter Witschey. Original mayamap.org implementation by the Maya Research Program. Supervised by Professor Lars Kotthoff.
