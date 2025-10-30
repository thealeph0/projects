def main():
    a = float(input("Value of side a: "))
    b = float(input("Value of side b: "))
    c = float(input("Value of side c: "))
    trianglearea(a,b,c)
    trianglearea(5,12,13)
    print(a)
    

def trianglearea(x,y,z):
    print("Triangle Area Calculator")
    
    s = (x+y+z)/2

    area = (s*(s-x)*(s-y)*(s-z))**0.5
    
    print(area)
    print(x)
    
    
main()
trianglearea(3,4,5)