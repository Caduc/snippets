#
#  to lookup a field in csv
#
import csv

search = "first"  #str(input())

print "searching for {}".format(search)

with open ("snippets.csv", "rt") as f:
	reader = csv.reader(f)
	for row in reader:
		if search == row [0]:
			print "found snippet name {} with a snippet of {}".format(row[0], row[1])
