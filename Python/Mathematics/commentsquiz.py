#Fibonacci with a twist
def mystery_function(n):
    a, b = 0, 1
    total = 0
    for _ in range(n): # for loop
        if b % 2 == 0: ## checks if value is even
            total += b ## sums up even values found
        a, b = b, a + b ## updates variables by shifting them up one up on Fib sequence
    return total ## function returns the sum of the even values of the Fib sequence

#Sums of Sums
def calculate_series(a, b):
    first = 1
    for i in range(1, a + 1):
        first *= i ## factorial up to 'a' value

    second = 0
    for j in range(1, b + 1):
        second += j ** 3 ## sum of each number cubed up to 'b'

    return first + second ## sum of a! and B^3 + ... + 3^3 + 2^3 + 1^3 


