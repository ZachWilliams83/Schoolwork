def somefunction(b):
    b.append(7)
    b = [4,5,6]
    b.append(8)
def main():
    a = [1,2,3]
    somefunction(a)
    print(a)
main()
#output  = [1, 2, 3, 7]