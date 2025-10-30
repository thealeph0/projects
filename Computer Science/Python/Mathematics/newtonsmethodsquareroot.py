def squareroot(a):
    approx = a/2
    count = 0
    cutoff = 0.0001
    while approx**2 - a > cutoff:
        approx = (approx + (a/approx))/2
        count += 1
        print('Performed', count ,' steps')
        print('Approximate square root of', a, 'is' , approx)
        print('Our approximation squared is', approx**2)
        
def main():
    num = int(input("Enter a non-negative number that you want to square root"))
    squareroot(num)
    
main()