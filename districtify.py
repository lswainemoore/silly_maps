from csv import (
    DictReader,
    DictWriter,
)

with open('attribute_table.csv') as f:
    r = DictReader(f)
    rows = [row for row in r]

target = sum(int(r['POP10']) for r in rows) / 11

left_to_right = sorted(rows, key=lambda row: row['x_center'])

district = 0
district_total = 0
for row in left_to_right:
    pop = int(row['POP10'])
    if (pop + district_total) > target:
        if (pop + district_total - target) < (target - district_total):
            row['x_district'] = district
            district += 1
            district_total = 0
        else:
            district += 1
            row['x_district'] = district
            district_total = pop
    else:
        row['x_district'] = district
        district_total += pop

down_to_up = sorted(rows, key=lambda row: row['y_center'])

district = 0
district_total = 0
for row in down_to_up:
    pop = int(row['POP10'])
    if (pop + district_total) > target:
        if (pop + district_total - target) < (target - district_total):
            row['y_district'] = district
            district += 1
            district_total = 0
        else:
            district += 1
            row['y_district'] = district
            district_total = pop
    else:
        row['y_district'] = district
        district_total += pop

with open('attribute_table2.csv', 'w') as f:
    w = DictWriter(f, ['BLOCKID10', 'x_district', 'y_district'])
    w.writeheader()
    for row in left_to_right:
        sub_row = {
            'BLOCKID10': row['BLOCKID10'],
            'x_district': row['x_district'],
            'y_district': row['y_district'],
        }
        w.writerow(sub_row)

