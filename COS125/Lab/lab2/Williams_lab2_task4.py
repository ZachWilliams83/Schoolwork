#A
cash = 1.5
if int(cash )*2.0 != int(cash *2.0):
    print("The devil is in the details.")
    # No prints will occur, the first integer == 2.0, while the second == 3

#B
temp = 40
if temp < 40:
    print("It is cold.")
    #No print, not inclusive.
elif temp < 70:
    print("It is mild.")
    #Print, 40 is less than 70.
elif temp < 90:
    print("It is hot.")
    #No print, statement already complete, will not continue to evaluate.
else:
    print("It is unbearable.")
    #No print, condition is satisfied above.

#C
i = 1
while i != 10:
    i = i + 1
    total = total + i
print(total)
#Will not print, total variable wasn't initialized outside of the loop.