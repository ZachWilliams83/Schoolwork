L = ["A", "B", "C", "D", "E"]
counter = 0
counter2 = 0
num = 0
inside = 1
iterator = 0
#Subtask 1
for i in range (10):
    for x in range(5):
        counter += 1
print(counter)
#Subtask 2
while num <4:
    num +=1
    inside = 0 
    while inside < 8:
        inside +=1
        counter2 +=1
print(counter2)
#Subtask 3
while iterator < len(L):
    print(L[iterator])
    iterator += 1
#Subtask 4
for i in range(len(L)):
    print(L[i])
