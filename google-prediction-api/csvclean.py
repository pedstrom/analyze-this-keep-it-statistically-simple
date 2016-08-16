import csv
with open('all.columns.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open('output.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            if row[4] != 'NA':
                val =  None
                if row[4] == '0':
                    val = "N"
                else:
                    val = "Y"
                row[4] = val
                writer.writerow(row)
        
            