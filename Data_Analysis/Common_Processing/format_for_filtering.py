import sys
import csv



input_csv = sys.argv[1]
isInDep = 0
isInBuild = 0

f = open(input_csv, "r")
output_csv = open("filys.csv", "w")
for n, line in enumerate(f):
	writer = csv.writer(output_csv)
	line2 = line.rstrip('\r\n')
	line_arr = line2.split(',')
	print line_arr
	new_line = []
	new_line.append(line_arr[1])
	new_line.append(line_arr[2])
	new_line.append(line_arr[3])
	new_line.append(line_arr[4])
	writer.writerow(new_line)
	# print line_arr
	






	# with open("output.csv", "a") as f:
	#     writer = csv.writer(f)
	#     writer.writerows(csv_lines)

