# Changelog

A log of significant changes and progress on the Maya Modern Map project.

## 2026-07-31

### Feature 26: Filter and flag sites with detailed structure data

- Added a "Show only sites with maps" checkbox beneath the search bar that narrows the list and map to the sites for which detailed structure data exists
- Flagged sites (Bed Rock, Blue Creek, Chum Balam-Nal, Grey Fox, Nojol Nah) show a small map icon beside their name in the site list, and a "Detailed site map available" badge in their popup
- The set of flagged sites was derived by matching each structure cluster to the nearest site in the main dataset by great-circle distance, since the survey folder names differ from the dataset's site names
- The filter combines with the search, rank, and radius filters and is carried in the shareable URL as data=1

### Feature 25: Structure footprint layer for the Blue Creek area

- Added a structures layer showing excavated building footprints for a cluster of sites in the Blue Creek area of northern Belize, drawn from supplied archaeological survey data
- Built data/maya_structures.geojson by reprojecting the supplied shapefiles from their local UTM grids (Clarke 1866, EPSG:26716 and EPSG:26916 variants) to WGS84, stripping Z coordinates, and merging the cleanest polygon and line sources into a single 1,852 feature file
- Redundant CAD exports and a corrupt source file were deliberately excluded to avoid drawing the same structures twice
- Footprints are drawn as warm stone polygons with a darker outline, in the style of an archaeological site plan, in a dedicated map pane
- The layer appears only from zoom 14 and above so it never clutters the regional view, can be toggled in the layers menu, and is carried in the shareable URL as struct=0 when off

### Feature 24: Measure tool for distance and area

- Added a measure tool to the bottom-right control stack that reports great-circle distances along a clicked path using the Haversine formula
- Clicking the first point again closes the shape and reports the enclosed area using the spherical excess formula, plus the perimeter
- Each leg carries a distance label at its midpoint, and each vertex names the nearest site
- The connecting line and its labels are drawn in separate map panes so the distance labels always sit above the line and stay readable
- The tool is mutually exclusive with the radius tool and exits on the Escape key or the Done button

## 2026-07-28

### Feature 23: Small watercourse layer

- Added a streams layer that renders small watercourses across the region, drawn from OpenStreetMap waterway data merged with supplied survey data for the Belize and Guatemala core
- Source data was clipped to the Maya region, reprojected to WGS84, and simplified to keep the file lightweight
- Streams appear from zoom 9 and above so the regional overview stays uncluttered, and can be toggled in the layers menu
- A supervisor-requested comparison of candidate basemaps informed keeping the existing four basemaps rather than adopting a terrain-only alternative

## 2026-07-27

### Feature 22: Low-zoom site labels

- Major site names now remain visible when zoomed out to the regional overview, addressing supervisor feedback that the map was hard to orient at low zoom
- Label density scales with zoom: only Major centres are named at the widest view, with Important, Medium, and all visible sites revealed progressively on zooming in

### Feature 21: Shareable view links

- The current map state (centre, zoom, search text, rank filters, view mode, basemap, layers, and any active radius) is now encoded in the URL
- A share button copies a link to the exact current view to the clipboard, with a confirmation toast
- Opening a shared link restores the full state, so a particular view can be sent to the supervisor or included in the dissertation

### Feature 20: Multi-select rank filtering

- Replaced the previous cumulative rank filter with independent multi-select pills, so any combination of significance levels can be shown at once
- The site count label reflects the selected combination in natural language

## 2026-07-11

### Feature 19: Performance optimisation

- Switched marker rendering to a shared canvas renderer so all 5,223 sites stay responsive during fast pan and zoom
- Rank 1 sites render in dedicated unclustered layers so their markers and labels are always present
- Analytics recalculation is debounced on map movement to keep panning smooth

### Feature 18: Mobile search drawer and bottom radius bar

- Reworked the mobile layout: the map is full screen with a gold Search tab on the left edge mirroring the Details tab on the right
- Tapping Search slides in a drawer with the search box, filters, and site list; selecting a site closes the drawer and flies the map to it
- The proximity tool on mobile now uses a dedicated bottom radius bar with its own slider, kept in sync with the desktop control
- Fixed points disappearing during pan and zoom on phones by switching circle markers to canvas rendering

### Feature 17: Mobile responsive layout

- Added the first responsive layout for narrow screens, with the floating panel becoming a bottom sheet that expands and collapses
- View pills and map buttons reposition above the sheet, and the details panel opens full width
- Desktop layout left unchanged

## 2026-07-06

### Feature 16: Analytics charts

- Added Chart.js 4.5.1 and the chartjs-plugin-datalabels plugin via the jsdelivr CDN
- By country: doughnut chart with legend and in-slice counts across Mexico, Guatemala, Belize, Honduras, and El Salvador
- By state / region: horizontal bar chart of the top 8 states by site count
- By archaeological rank: vertical bar chart from Major centres to Minimal remains
- All three charts and the summary count update live whenever the search, rank, or radius filters change

## 2026-07-05

### Fix: site labels

- Moved labels into a dedicated Leaflet pane (z-index 640) so they always render above markers and clusters
- Adjusted zoom thresholds so Major site names are visible from the default overview zoom

### Feature 15: Progressive site labels

- Site names now appear directly on the map without clicking, addressing supervisor feedback
- Labels reveal progressively by rank and zoom level: Major centres first, then Important, Medium, and all visible sites when fully zoomed in
- White halo text treatment keeps labels legible on all four basemaps
- Labels are limited to the current map bounds and refresh on pan and zoom for performance
- Labels are hidden in Heat view where individual names would obscure the density surface

## 2026-07-04

### Feature 14: Details tab and analytics panel

- Added a vertical gold Details tab pinned to the right edge of the screen
- Clicking it slides in a 450px analytics panel with a live summary count and three chart sections
- Panel closes via the close button or the Escape key

## 2026-07-02

### Feature 12: Draggable panel

- The floating panel can now be repositioned by dragging the handle at its top
- Dragging is clamped to the viewport so the panel can never be lost off-screen
- Touch input supported; handle highlights gold while dragging
- Dragging is disabled at mobile widths ahead of the responsive layout work

## 2026-07-01

### Feature 11: Radius tool

- Proximity filtering implemented with the Haversine great-circle formula
- Activating Radius turns the cursor into a crosshair; clicking the map sets a centre and draws a red circle
- Interactive slider from 10 to 500 km resizes the circle and updates markers, list, and counts in real time
- Stacks with the search and rank filters; Escape key exits the tool

## 2026-06-30

### Feature 8: View mode toggle

- Added Points, Bubbles, and Heat view pills in the bottom-left corner
- Bubbles view renders translucent red circles sized by archaeological rank, with count clusters at low zoom
- Heat view renders a Leaflet.heat density heatmap with a blue-to-red gradient
- All views respect the active search and filter state

### Feature 6: Scrollable site list

- Alphabetical list of all visible sites showing name, country, and state
- Clicking an item flies to the site, expands its cluster, and opens the popup
- List selection stays in sync with marker popups; the active item is highlighted gold

## 2026-06-29

### Feature 5: Rank filter pills

- Major, Important, Medium, and Minor pills filter sites cumulatively by rank
- Clicking the active pill again clears the filter; combines with the search query

### Feature 4: Search bar and Radius button

- Live search across site name, country, and state with a dynamic count readout
- Radius button added to the search row as a placeholder for the proximity tool

### Feature 3: Locate button and panel scaffolding

- Find-my-location control with a Google-style pulsing blue dot and fly-to animation
- Floating panel added in the top-left as the home for search, filters, and the site list

## 2026-06-28

### Feature 2: Custom basemap switcher

- Added four basemap options: OpenStreetMap (default), Esri Topo, Dark (CartoDB), and Satellite (Esri)
- Replaced the default Leaflet layers control with a custom floating square icon button in the bottom-right
- Implemented a popover panel that opens above the button on click, showing each basemap with name, description, and active-state indicator
- Active basemap highlighted with a gold check mark and gold text
- Clicking outside the popover closes it

### Feature 1: Design colour palette and typography

- Applied design tokens for gold accent (#e2b96f), deep navy map background (#0e1424), and dark popup background (#16213e)
- Switched to the system sans-serif font stack
- Dark-themed popups with gold title text, uppercase sub-line for country and state, and rank badge with pill styling
- Restyled Leaflet zoom controls and attribution to match the design language
- Customised marker cluster appearance to use translucent gold instead of default blue

### Core map implementation

- Replaced the placeholder index.html with a working Leaflet.js implementation
- Map loads Leaflet v1.9.4 from the unpkg CDN with subresource integrity checks
- Default view centred on the Maya region at coordinates (16.5, -89.5), zoom level 6
- OpenStreetMap configured as the default basemap
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

### Data conversion pipeline

- Implemented scripts/convert_sites.py to convert the EAAMS shapefile to GeoJSON
- Script handles CRS reprojection to WGS84, filtering of unnamed records, attribute normalisation, and UTF-8 encoding of non-ASCII site names
- Updated to use real EAAMS field names: BWNAME, BWCOuntry, BWState, rank, NOTES
- Output written to data/maya_sites.geojson as an RFC 7946 compliant FeatureCollection
