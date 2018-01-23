import sys
import csv



input_csv = sys.argv[1]


f = open(input_csv, "r")
output_csv = open("rq.csv", "w")
for n, line in enumerate(f):
    writer = csv.writer(output_csv)
    line2 = line.rstrip('\r\n')
    line_arr = line2.split(',')
    if line_arr[4] == 'depe0' and line_arr[5] == 'scope' and line_arr[6] == 'system':
    	for x in xrange(8):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'depe0' and line_arr[5] == 'scope' and line_arr[6] == 'test':
    	for x in xrange(8):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'depe0' and line_arr[5] == 'scope' and line_arr[6] == 'runtime':
    	for x in xrange(8):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2) 
        for x in xrange(8):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        	writer.writerow(line_arr_2) 
    elif line_arr[4] == 'depe0' and line_arr[5] == 'artifactId':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'depm0' and line_arr[5] == 'scope' and line_arr[6] == 'system':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'depm0' and line_arr[5] == 'scope' and line_arr[6] == 'test':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'depm0' and line_arr[5] == 'scope' and line_arr[6] == 'runtime':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2) 
        for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        	writer.writerow(line_arr_2) 
    elif line_arr[4] == 'depm0' and line_arr[5] == 'artifactId':
    	for x in xrange(5):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'prer0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        writer.writerow(line_arr_2) 
    elif line_arr[4] == 'modu0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        writer.writerow(line_arr_2) 
    elif line_arr[4] == 'cima0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        writer.writerow(line_arr_2) 
    elif line_arr[4] == 'pack0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        writer.writerow(line_arr_2) 
    elif line_arr[4] == 'url0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        writer.writerow(line_arr_2)
    elif line_arr[4] == 'issu0':
    	line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        writer.writerow(line_arr_2)  
    elif line_arr[4] == 'plur0' and line_arr[5] == 'url':
    	for x in xrange(3):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2) 
    elif line_arr[4] == 'repo0' and line_arr[5] == 'url':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'dist0' and line_arr[5] == 'url':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-enforcer-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-compiler-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-resources-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-surefire-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2) 
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'findbugs-maven-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-surefire-report-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-jar-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-war-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-assembly-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-source-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-dependency-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-shade-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-gpg-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-install-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-pmd-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'artifactId' and line_arr[6] == 'maven-deploy-plugin':
    	for x in xrange(10):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        	writer.writerow(line_arr_2)  
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'validate':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "validate"]
        	writer.writerow(line_arr_2) 
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'generate-resources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'generate-sources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'process-sources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'process-resources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'compile':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "compile"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'generate-test-sources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'generate-test-resources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'process-test-sources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'process-test-resources':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'test-compile':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'test':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "test"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'package':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'prepare-package':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'process-classes':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "packaging"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'pre-integration-test':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'post-integration-test':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'integration-test':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'verify':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'install':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "install"]
        	writer.writerow(line_arr_2)
    elif line_arr[4] == 'buil0' and line_arr[5] == 'phase' and line_arr[6] == 'deploy':
    	for x in xrange(4):
    		line_arr_2 = [line_arr[0], line_arr[1], line_arr[2], "deploy"]
        	writer.writerow(line_arr_2)
    # print line_arr
    


