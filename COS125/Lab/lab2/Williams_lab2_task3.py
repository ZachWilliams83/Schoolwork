x = 10
char = "a"
num = 0
odd = 0
sum = 0

while x > 0:
    print (x)
    x -= 1
while x <= 10:
    print (x)
    x += 1
while char != "q":
    char = input("Please enter a single character (Enter q to Quit). ")
while num != 1000:
    num += 1
    if num % 2 == 1:
        sum += num
print(sum)