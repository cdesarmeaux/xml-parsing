import sys
import csv



input_csv = sys.argv[1]
isInDep = 0
isInBuild = 0
isInPrereqs = 0
isInModules = 0
isInCim = 0
isInPack = 0
isInUrl = 0
isInIssueMan = 0
isInPluRepo = 0
isInDepMan = 0
isInDistMan = 0
isInRepos = 0

f = open(input_csv, "r")
output_csv = open("pre_porcessed.csv", "w")
for n, line in enumerate(f):
    writer = csv.writer(output_csv)
    line2 = line.rstrip('\r\n')
    line_arr = line2.split(',')
    print line_arr
    if n == 0:
        continue
    elif line_arr[6] == 'dependencies' and line_arr[7] == '1':
        isInDep = 1
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('depe0')
    elif line_arr[6] == 'build' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 1
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('buil0')
    elif line_arr[6] == 'prerequisites' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 1
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('prer0')
    elif line_arr[6] == 'modules' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 1
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('modu0')
    elif line_arr[6] == 'ciManagement' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 1
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('cima0')
    elif line_arr[6] == 'packaging' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 1
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('pack0')
    elif line_arr[6] == 'url' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 1
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('url0')
    elif line_arr[6] == 'issueManagement' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 1
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('issu0')
    elif line_arr[6] == 'pluginRepositories' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 1
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('plur0')
    elif line_arr[6] == 'dependencyManagement' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 1
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('depm0')
    elif line_arr[6] == 'distributionManagement' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 1
        isInRepos = 0
        line_arr.append('dist0')
    elif line_arr[6] == 'repositories' and line_arr[7] == '1':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 1
        line_arr.append('repo0')
    elif line_arr[6] == 'project':
        isInDep = 0
        isInBuild = 0
        isInPrereqs = 0
        isInModules = 0
        isInCim = 0
        isInPack = 0
        isInUrl = 0
        isInIssueMan = 0
        isInPluRepo = 0
        isInDepMan = 0
        isInDistMan = 0
        isInRepos = 0
        line_arr.append('na')
    elif isInDep == 1:
        line_arr.append('depe0')
    elif isInBuild == 1:
         line_arr.append('buil0')
    elif isInPrereqs == 1:
         line_arr.append('prer0')
    elif isInModules == 1:
         line_arr.append('modu0')
    elif isInCim == 1:
         line_arr.append('cima0')
    elif isInPack == 1:
         line_arr.append('pack0')
    elif isInUrl == 1:
         line_arr.append('url0')
    elif isInIssueMan == 1:
         line_arr.append('issu0')
    elif isInPluRepo == 1:
         line_arr.append('plur0')
    elif isInDepMan == 1:
         line_arr.append('depm0')
    elif isInDistMan == 1:
         line_arr.append('dist0')
    elif isInRepos == 1:
         line_arr.append('repo0')
    elif isInDep == 0 and isInBuild == 0 and isInPrereqs == 0 and isInModules == 0 and isInCim == 0 and isInPack == 0 and isInUrl == 0 and isInIssueMan == 0 and isInPluRepo == 0 and isInDepMan == 0 and isInDistMan == 0 and isInRepos == 0:
         line_arr.append('na')
    writer.writerow(line_arr)
    # print line_arr
    


