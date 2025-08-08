import csv
from parts.models import Part 

with open('/storage/emulated/0/mystorage/parts_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Part.objects.create(
            part_number=row['PART NUMBER'],
            oem=row['OEM'],
            description=row['DESCRIPTION'],
            shelf=row['SHELF'],
            level=row['LEVEL'],
            row_position=row['ROW']
        )
