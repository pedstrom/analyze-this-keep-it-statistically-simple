import csv
with open('test-onlycopy.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open('test-only-quotes.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            new_row = map(str.strip, row)
            writer.writerow(new_row)
        
            