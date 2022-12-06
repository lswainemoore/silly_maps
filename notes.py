# this is for CenPop2010_Mean_TR51/tl_2020_51_tract

from csv import DictReader
with open('/Users/lsm/stuff/silly_maps/silly_maps/CenPop2010_Mean_TR51.txt') as f:
    r = DictReader(f)
    rows = [row for row in r]

for row in rows:
    row['combined_row'] = (row['COUNTYFP'], row['TRACTCE'])
    row['lat_num'] = float(row['LATITUDE'][1:])
    row['long_num'] = float(row['LONGITUDE'][1:])
    row['pop'] = int(row['POPULATION'])

left_to_right = sorted(rows, key=lambda row: row['long_num'])
target = sum(r['pop'] for r in rows) / 11


left_to_right_dict = {}
for row in left_to_right:
    left_to_right_dict[(row['COUNTYFP'], row['TRACTCE'])] = row

layer = iface.activeLayer()

layer.startEditing()
for feature in layer.getFeatures():
    layer.changeAttributeValue(feature.id(), 12, left_to_right_dict[(feature['COUNTYFP10'], feature['TRACTCE10'])]['district'])
    layer.commitChanges()




