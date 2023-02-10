

def FunctionA(a,b):
    return FunctionB(a // b)

def FunctionB(c):
    return FunctionC(c-1.5)

def FunctionC(d):
    return FunctionD(int(d))

def FunctionD(e):
    return 100 / e

def main():
    x = 10
    y = 5.0
    answer = FunctionA(x,y)
    print(answer)

main()