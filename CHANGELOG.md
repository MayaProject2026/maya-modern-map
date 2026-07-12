# Changelog

A log of significant changes and progress on the Maya Modern Map project.

## 2026-07-12

### Feature 18: Mobile search drawer and bottom radius bar

- On phones the map is now full screen with a gold Search tab on the left edge, mirroring the Details tab on the right
- Tapping Search slides in a drawer with the search box, rank filters, and the full site list; picking a result closes the drawer and flies to the site
- Activating the radius tool on mobile closes the drawer and shows a slim bottom bar with the distance slider and live count; Done dismisses it
- Desktop layout is unchanged

## 2026-07-11

### Feature 17: Mobile responsive layout

- First mobile layout pass introducing a bottom sheet panel sized for small screens
- Map controls and view pills repositioned to remain reachable above the sheet

### Fix: mobile rendering and interaction

- Switched marker rendering to canvas (Leaflet preferCanvas) so all 5,223 points stay responsive on mobile GPUs during fast pan and zoom
- Made the sheet toggle reliable on iOS by handling touchend directly with a double toggle guard
- Debounced analytics recalculation on map movement to keep momentum panning smooth

## 2026-07-09

### Match details panel and home control to the original design

- Rebuilt the Details panel to the design specification: Maya Civilisation title block, introductory text, Sites by Country doughnut with the design colour palette, Top Regions bar chart, Sites by Significance bars, Best Areas to Visit cards, and a data source note
- Sites by Significance rendered as custom HTML bars that rescale to the sites in the current view
- Replaced the custom home button with a standard Leaflet bar control using a house glyph, positioned directly under the zoom controls

### Fix: analytics scoped to the current map view (closes issue 4)

- The Details panel counts and all charts now reflect only the sites inside the current viewport
- Panning and zooming refreshes the analytics live

## 2026-07-08

### Fix: major site visibility and label placement (closes issues 1, 2, and 3)

- Rank 1 sites are no longer clustered; they render as individual larger gold markers at every zoom level so their labels never float without a point
- Added greedy collision aware label placement: higher significance sites win, overlapping lower rank labels are skipped
- At zoom 10 and above the rank cutoff is removed so every visible site is labelled where space allows

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
