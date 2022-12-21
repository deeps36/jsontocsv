# Python program to convert
# JSON file to CSV


import json
import csv


# Opening JSON file and loading the data
# into the variable data
# ans.json is json file for the input
with open('/media/io-fes/Data1/DriveG/Deep/ans.json') as json_file:
	data = json.load(json_file)

json_data = data['response']

# now we will open a file for writing
# response.csv is the output file 
data_file = open('/media/io-fes/Data1/DriveG/Deep/response.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for deep in json_data:
	if count == 0:

		# Writing headers of CSV file
		header = deep.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(deep.values())

data_file.close()
