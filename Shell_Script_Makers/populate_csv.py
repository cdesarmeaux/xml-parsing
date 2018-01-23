import sys
import csv


f = open("project_names.txt", "r")
p = f.readlines()
q = []
n = 1
q.append('#!/bin/sh\n\n\n')
for line in p:
	if n==101:
		break;
	temp = line.split(' ')
	new_line = str(temp[0])
	q.append('python alternate_parser.py log_file_'+ str(n) +'.txt ' + new_line + '\n')
	n = n+ 1

f.close()

f = open("populate_csv.sh", "w")
f.write(''.join(q))
f.close
