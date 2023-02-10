x = 0
y = 0
a = 0
b = 0
c = 0
t = 0.0
i = 0
j = 0
k = 0

if x > 1:
    x = 1
elif x < -1:
    x = -1
else:
    x = 0
if y > 10 and y < 20:
    print("Yes")
else:
    print("No")
if a == b or a == c:
    print("Correct")
else:
    print("Incorrect")
if (t - int(t)) == 0:
    int(t)
if i == 0 and j == 0 and k != 0:
    print(True)
elif i != 0 and j == 0 and k == 0:
    print(True)
elif i == 0 and j != 0 and k == 0:
    print(True)
else:
    print(False)
