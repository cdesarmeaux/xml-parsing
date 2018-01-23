import sys
import os
import csv
import xml.etree.ElementTree as ET



i = 0
initial = 0
start = 0
end = 0
p = 0
line_begin = 0
xml_count = 0
dif = 0
n_initial = 0
tmp = ''
changes = []
removed = []
commit_id = ''
temp_commit_id = ''
date = ''
temp_date = ''
changeId = 0
done = 0
sawBeginning = 0
commit_number = 0
in_file = 0
total_commits = 0
line_tracker = 0
csv_lines = []
log_file = sys.argv[1]
proj_name = sys.argv[2]
csv_line1 = []


def myDFS(graph,start,path=[], path_tag=[], path_attr=[]):
	if len(start) != 0: 
		path = path + [start]
		path_tag=path_tag+[start.tag]
		path_attr = path_attr+[start.tag]
	if len(start) == 0:
		path = path + [start]
		path_tag=path_tag+[start.tag]
		path_attr = path_attr+[start.tag, start.text]
		paths_tag.append(path_tag)
		paths_attr.append(path_attr)
	for child in start:
		if child not in path:
			myDFS(graph,child,path, path_tag, path_attr)


def xml_format(path=[]):
	output_string = ''
	n = 0
	for element in path:
		if n==0:
			output_string = "<" + str(element) + ">"
		else:
			output_string = output_string + ".<" + str(element) + ">"
		n = n + 1
	return output_string


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""




f = open(log_file, "r")
for n, line in enumerate(f):
	if line[:7] == 'commit ':
		total_commits = total_commits + 1

f.close()


commit_comment_line = 1
metadata = []
temp_metadata = []
new = []
cn = 1
# get the initial pom.xml
xml_tracker = open("xml_tracker.xml", "w")
f = open(log_file, "r")
for n, line in enumerate(f):
	if line == '--- /dev/null\n':
		initial = 1
		start = n+2
	elif line[:1] == '+' and initial > 0 and n >= start and i == 0:
		string = line.replace(line[:1],'')
		if ('<project' not in string) or sawBeginning == 1:
			xml_tracker.write(string)
		else:
			string = '<project>\n'
			xml_tracker.write(string)
			sawBeginning = 1
	elif line[:6] == 'commit' and initial > 0 and i == 0: # or id EOF
		n_initial = n
		initial = 0
		xml_tracker.close()
		done = 1
		sawBeginning = 0
	elif '</project>' in line and '<!--' not in line and '-->' not in line:
		commit_comment_line = 1
	elif '<project' in line and '<!--' not in line and '-->' not in line and done == 1:
		commit_comment_line = 0
	elif line[:8] == 'Author: ' and done == 1:
		temp_metadata = []
		temp_metadata.append(proj_name)
		temp_metadata.append(find_between(line, "<", "@"))
	elif line[:6] == 'Date: ' and done == 1:
		temp = line[8:]
		temp_metadata.append(temp[:32-8])
		temp_metadata.append('null')
		temp_metadata.append(cn)
		metadata.append(temp_metadata)
		cn = cn + 1
	if commit_comment_line == 0 or ('</project>' in line and '<!--' not in line and '-->' not in line):
		if '</project>' in line and '<!--' not in line and '-->' not in line:
			new.append(line)
			new.append('----------')
		else:
			new.append(line)
f.close()






if total_commits > 1:

	for i in xrange(0,total_commits-1):
		xml_tracker_2 = open("xml_tracker_2.xml", "w")
		sawBeginning = 0
		commit_number = 0
		for n, line in enumerate(new):
			if line == '----------':
				commit_number = commit_number + 1
			elif commit_number == i+1:
				if line[:1] == '+':
					string = line.replace(line[:1],' ')
					if ('<project' not in string) or sawBeginning == 1:
						xml_tracker_2.write(string)
					else:
						string = '<project>\n'
						xml_tracker_2.write(string)
						sawBeginning = 1
				elif line[:1] != '-':
					string = line
					if (('<project' not in string) or sawBeginning == 1):
						xml_tracker_2.write(string)
					elif ('commit ' != line[:7]):
						string = '<project>\n'
						xml_tracker_2.write(string)
						sawBeginning = 1


		xml_tracker_2.close()


		if os.stat('xml_tracker_2.xml').st_size == 0:
			break


		new_tree = ET.parse('xml_tracker_2.xml')
		new_root = new_tree.getroot()
		new_path = []
		new_path_tag = []
		new_path_attr = []
		new_paths_tag = []
		new_paths_attr = []


		old_tree = ET.parse('xml_tracker.xml')
		old_root = old_tree.getroot()
		old_path = []
		old_path_tag = []
		old_path_attr = []
		old_paths_tag = []
		old_paths_attr = []


		paths_tag = []
		paths_attr = []

		myDFS(new_tree, new_root,new_path, new_path_tag, new_path_attr)
		new_paths_tag = paths_tag
		new_paths_attr = paths_attr


		paths_tag = []
		paths_attr = []

		myDFS(old_tree, old_root,old_path, old_path_tag, old_path_attr)
		old_paths_tag = paths_tag
		old_paths_attr = paths_attr

		print temp_metadata

		for temp_metadata in metadata:
			if temp_metadata[4] == i+1:
				csv_line1 = temp_metadata


		a = 0
		for n_path in new_paths_attr:
			if n_path[:len(n_path)-1] not in old_paths_tag:
				truncated = n_path[:len(n_path)-1]
				level = 0
				for tag in truncated:
					csv_line = [csv_line1[0], csv_line1[1] ,csv_line1[2], csv_line1[3], csv_line1[4], '/pom.xml', tag, level, n_path[len(n_path)-1], 'added']
					csv_lines.append(csv_line)
					level = level + 1
			a = a + 1

		r = 0
		for o_path in old_paths_attr:
			if o_path[:len(o_path)-1] not in new_paths_tag:
				truncated = o_path[:len(o_path)-1]
				level = 0
				for tag in truncated:
					csv_line = [csv_line1[0], csv_line1[1] ,csv_line1[2], csv_line1[3], csv_line1[4], '/pom.xml', tag, level, o_path[len(o_path)-1], 'removed']
					csv_lines.append(csv_line)
					level = level + 1
			r = r + 1

		m = 0
		for n_path in new_paths_attr:
			if n_path[:len(n_path)-1] in old_paths_tag and n_path not in old_paths_attr:
				truncated = n_path[:len(n_path)-1]
				level = 0
				for tag in truncated:
					csv_line = [csv_line1[0], csv_line1[1] ,csv_line1[2], csv_line1[3], csv_line1[4], '/pom.xml', tag, level, n_path[len(n_path)-1], 'modified']
					csv_lines.append(csv_line)
					level = level + 1
			m = m + 1




		if i != total_commits-2:
			open("xml_tracker.xml", "w").writelines([l for l in open("xml_tracker_2.xml").readlines()])




	with open("output.csv", "a") as f:
	    writer = csv.writer(f)
	    writer.writerows(csv_lines)






