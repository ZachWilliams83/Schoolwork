alist = [4, 5, 88, 32, 99, 88, 73, 68, 91, 1024]
for i in range(len(alist)):
    num = alist[i]
    while num % 2 == 0:
        num = num / 2
    print(num)
