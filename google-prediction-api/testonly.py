import csv
with open('all-columns-noheader.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open('test-only.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            if row[3] == "Test": #only get the Test Data
                writer.writerow(row)

'''
out_file = open("test-only.csv", "w")
in_file = open('all-columns-noheader.csv', 'r')
for line in in_file:
	if ",Test," in line:
	    out_file.write(line)
out_file.close()
in_file.close()
'''