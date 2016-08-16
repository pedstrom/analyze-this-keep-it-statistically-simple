import csv
with open('smm-training-quotes.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open('onlyyes.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            if row[0] == 'Y':
                writer.writerow(row)
        
            