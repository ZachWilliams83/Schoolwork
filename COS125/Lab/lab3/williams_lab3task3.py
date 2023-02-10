mylist = [2, 11, 12, 45, 52, 808, 7, 68, 91, 1013]
first_names = ['Lisa', 'Bob', 'Carl', 'Mohammed', 'Vlad', 'Aina']
last_names = ['Smith', 'Zhang', 'Karlson', 'Lee', 'Numan', 'Musa']
c = 0
counter = 0
#Subtask 1
for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        mylist[i] = mylist[i] // 2
print(mylist)
#Subtask 2
while c != (len(first_names)):
    #print(first_names[c], last_names[c])
    c += 1
#Subtask 3
while counter < 6 :
    print(first_names[(counter+2)%6], last_names[counter])
    counter += 1




