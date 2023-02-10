def Hello():
    print("Hello world.")
Hello()

def HelloTo(name):
    print(f"Hello, {name}!")
HelloTo("Joe")

def Distance(x1,y1,x2,y2):
    d = (((x2 - x1)**2) + ((y2 - y1)**2)**0.5)
    print(f"The distance is {d}")
Distance(1,1,7,7)