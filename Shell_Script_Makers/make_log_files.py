import sys
import csv


log_file = sys.argv[1]

f = open(log_file, "r")
p = f.readlines()
q = []
n = 1
q.append('#!/bin/sh\n\n\n')
for line in p:
	temp = line.split(' ')
	new_line_temp = str(temp[2])
	new_line = new_line_temp.split('/')
	output_line = 'cd /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/Data_Mining/Maven_Repositories/' +  new_line[4] + '\n'
	q.append(output_line)
	q.append('git log --no-prefix --reverse -p -U100000 "$(find . | egrep pom.xml)" > /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/Data_Mining/Log_Files/log_file_'+ str(n) +'.txt\n')
	q.append('cd /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/Data_Mining/Maven_Repositories/')
	n = n+ 1

f.close()

f = open("/Users/casimirdesarmeaux/Documents/McGill/ECSE-456/Data_Mining/Shell_Scripts/get_log_files.sh", "w")
f.write(''.join(q))
f.close
