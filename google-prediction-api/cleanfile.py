out_file = open("all-columns-noheader-clean.csv", "w")
in_file = open('all-columns-noheader.csv', 'r')
for line in in_file:
	if ",Test," not in line:
	    out_file.write(line)
out_file.close()
in_file.close()