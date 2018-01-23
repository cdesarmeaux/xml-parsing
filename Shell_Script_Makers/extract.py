import sys
import csv


log_file = sys.argv[1]

f = open(log_file, "r")
p = f.readlines()
q = []
q.append('#!/bin/sh\n\n\n')
n = 1
for line in p:
	new_line_temp = line.rstrip()
	new_line = new_line_temp.split('/')
	output_line = 'git clone ' + new_line_temp + '.git' + ' /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/' + new_line[4] + '\n'
	output_line2 = 'cd /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/' +  new_line[4] + '\n'
	q.append(output_line)
	q.append(output_line2)
	q.append('git log --no-prefix --reverse -p -U100000 "$(find . | egrep pom.xml)" > /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/log_file_'+ str(n) +'.txt\n')
	q.append('cd /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/\n')
	q.append('python /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/alternate_parser.py log_file_'+ str(n) +'.txt ' + new_line[4] + '\n')
	q.append('rm -rf /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/' +  new_line[4] + '\n')
	q.append('rm -r /Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/log_file_'+ str(n) +'.txt\n')
	n = n + 1
f.close()


f = open("/Users/casimirdesarmeaux/Documents/McGill/ECSE-456/WSH/cloning_script.sh", "w")
f.write(''.join(q))
f.close


