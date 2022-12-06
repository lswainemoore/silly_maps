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



TODO
- so much...i'm adding after the fact here.
- but among them, maybe make it interactive. that would be cool.


LINKS
here are a bunch of links i had open while working on this:
https://gis.stackexchange.com/questions/61862/simple-thematic-mapping-of-shapefile-using-python
https://geopandas.org/en/stable/docs/user_guide/mapping.html
https://geopandas.org/en/stable/getting_started/install.html
https://stackoverflow.com/questions/36732075/geopandas-postgis-connection
https://www.postgresqltutorial.com/postgresql-python/connect/
https://www.google.com/search?q=geopandas+remove+borders&rlz=1C5CHFA_enUS916US919&oq=geopandas+remove+borders&aqs=chrome..69i57.15735j0j7&sourceid=chrome&ie=UTF-8
https://stackoverflow.com/questions/55141628/matplotlib-ax-to-figure-extent-remove-whitespace-borders-everything-for-plot
https://stackoverflow.com/questions/55759070/geopandas-mapplotlib-how-do-i-plot-without-an-outline-around-any-shape
https://stackoverflow.com/questions/47283912/saving-plot-with-high-resolution-image/47283983
http://darribas.org/gds15/content/labs/lab_03.html
https://stackoverflow.com/questions/9295026/how-to-remove-axis-legends-and-white-padding
https://stackoverflow.com/questions/39870642/matplotlib-how-to-plot-a-high-resolution-graph
https://stackoverflow.com/questions/19555525/saving-plots-axessubplot-generated-from-python-pandas-with-matplotlibs-savefi
https://stackoverflow.com/questions/22841206/calculating-cumulative-sum-in-postgresql
https://stackoverflow.com/questions/12618232/copy-a-few-of-the-columns-of-a-csv-file-into-a-table
https://stackoverflow.com/questions/3279086/importing-csv-file-into-postgresql
https://stackoverflow.com/questions/18297980/pg-copy-error-invalid-input-syntax-for-integer
https://stackoverflow.com/questions/11774654/how-to-make-postgres-copy-ignore-first-line-of-large-txt-file
https://gis.stackexchange.com/questions/41799/adding-shapefiles-to-postgis-database
https://gis.stackexchange.com/questions/202839/plotting-large-shapefiles-with-matplotlib
https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib/152331#152331
https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f
https://dataschool.com/learn-sql/export-to-csv-from-psql/
https://dataschool.com/learn-sql/how-to-export-data-to-csv-or-excel/
https://geopandas.org/en/stable/docs/user_guide/mapping.html
https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib

