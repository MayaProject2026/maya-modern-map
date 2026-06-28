# Changelog

A log of significant changes and progress on the Maya Modern Map project.

## 2026-06-29

### Feature 2: Custom basemap switcher

- Added four basemap options: OpenStreetMap (default), Esri Topo, Dark (CartoDB), and Satellite (Esri)
- Replaced the default Leaflet layers control with a custom floating square icon button in the bottom-right
- Implemented a popover panel that opens above the button on click, showing each basemap with name, description, and active-state indicator
- Active basemap highlighted with a gold check mark and gold text
- Clicking outside the popover closes it
- Layers button toggles gold when popover is open

### Feature 1: Design colour palette and typography

- Applied design tokens for gold accent (#e2b96f), deep navy map background (#0e1424), and dark popup background (#16213e)
- Switched to the system sans-serif font stack
- Dark-themed popups with gold title text, uppercase sub-line for country and state, and rank badge with pill styling
- Restyled Leaflet zoom controls and attribution to match the design language
- Customised marker cluster appearance to use translucent gold instead of default blue

## 2026-06-28

### Core map implementation

- Replaced the placeholder index.html with a working Leaflet.js implementation
- Map loads Leaflet v1.9.4 from the unpkg CDN with subresource integrity checks
- Default view centred on the Maya region at coordinates (16.5, -89.5), zoom level 6
- OpenStreetMap configured as the default basemap
- Mobile viewport meta tag added to support touch interaction
- Full-viewport responsive layout with loading indicator

### Maya sites data

- Generated maya_sites.geojson via the convert_sites.py pipeline
- Output contains 5,223 named Maya archaeological sites from the EAAMS dataset
- Filtered out 1,118 unnamed records
- Coordinate reference system: WGS84 (EPSG:4326)
- File size: 951 KB minified

### Sites loaded on map

- All 5,223 sites rendered as gold circle markers
- Marker clustering enabled (Leaflet.markercluster) to handle density
- Site popup shows name, country, state, and archaeological rank

### Foundation and infrastructure

- Created GitHub repository at github.com/MayaProject2026/maya-modern-map
- Configured MIT licence and .gitignore for Python and shapefile artifacts
- Set up project README with full description, technology stack, and architecture overview
- Enabled GitHub Pages deployment from the main branch
- Live site available at https://mayaproject2026.github.io/maya-modern-map/

### Repository structure

- Created scripts/ folder with documentation for the data conversion pipeline
- Created data/ folder with documentation describing the EAAMS source data and CRS conventions

### Data conversion pipeline

- Implemented scripts/convert_sites.py to convert the EAAMS shapefile to GeoJSON
- Script handles CRS reprojection to WGS84, filtering of unnamed records, attribute normalisation, and UTF-8 encoding of non-ASCII site names
- Updated to use real EAAMS field names: BWNAME, BWCOuntry, BWState, rank, NOTES
- Output written to data/maya_sites.geojson as an RFC 7946 compliant FeatureCollection
