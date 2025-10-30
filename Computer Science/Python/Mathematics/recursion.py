def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n*factorial_rec(n-1)
    
#def main():
    #print(factorial_rec(5))
    
# direct solution using for loop
def fib(n):
    prev_fib = 0
    current_fib = 1
    for i in range(2, n+1):
        current_fib, prev_fib = current_fib + prev_fib , current_fib
        
    return current_fib

def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)

print(fib(10))
print()
print(fib_rec(10))

    
#main()
    
