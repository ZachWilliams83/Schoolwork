labdata = open('lab7_data.txt', encoding = 'utf8')
rewrite = open('lab7_data_clean.txt', 'w')
for i in labdata:
    formatted = i.strip().strip(',').split(';')
    if int(formatted[2]) > 10000:
        i.strip(',')
        rewrite.write(formatted[0::])
labdata.close()
rewrite.close()