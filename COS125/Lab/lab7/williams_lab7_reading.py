# Task 1
labdata = open('lab7_data.txt', encoding = 'utf8')
printer = labdata.readlines()
print(printer)

# Task 2
labdata = open('lab7_data.txt', encoding = 'utf8')
for eachLine in labdata:
    splitline = eachLine.strip().split(';')
    if splitline[1] == 'Germany':
        print(splitline[0], splitline[2::])

# Task 3
numdata = open('lab7_data.txt', encoding = 'utf8')
for eachLine in numdata:
    splitline = eachLine.split(';')
    if splitline[1]
