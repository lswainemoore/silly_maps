SOURCES

CenPop2010_Mean_TR51.txt
	- https://www2.census.gov/geo/docs/reference/cenpop2010/tract/CenPop2010_Mean_TR51.txt
	- https://www.census.gov/geographies/reference-files/time-series/geo/centers-population.2010.html

tl_2020_51_tract
	- https://www2.census.gov/geo/tiger/TIGER2020/TRACT/
	- https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html

tabblock2010_51_pophu
- https://www2.census.gov/geo/tiger/TIGER2010BLKPOPHU/

cb_2018_us_state_500k
- https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html


1) import into qgis, and open attribute table
2) add new fields ("toggle edit mode", then "open field calculator", then add new fields with formulas "x/y($geometry)" -- be sure to pick real number, not int)
3) export table as csv
4) run districtify.py
5) layer -> add layer -> add delimited text layer: import without geometry
6) join data: layer properties -> join -> plus sign
7) color ramp using new fields: layer properties -> categorized -> select field -> classify
8) ok this is ugly, but to get rid of borders: double click a row, then select simple fill and set the border color to be the same as fill

attempted originally to do 3-6 inside qgis using something like
```
district = 0
district_total = 0
layer = iface.activeLayer()
for feature in layer.getFeatures(QgsFeatureRequest().addOrderBy('x_center')):
    if (feature['POP10'] + district_total) > target:
        if (feature['POP10'] + district_total - target) < (target - district_total):
            row_district = district
            district += 1
            district_total = 0
        else:
            district += 1
            row_district = district
            district_total = feature['POP10']
    else:
        row_district = district
        district_total += feature['POP10']
    layer.changeAttributeValue(feature.id(), 11, row_district)
    layer.commitChanges()
``` (after creating field to put it in)
but it took wayyy too long.
