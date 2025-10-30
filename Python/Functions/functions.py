import math

def sum_to_n(num):
    return int((num * (num+1))/2)

print(sum_to_n(10))

def get_next_prime(n):
    if n < 2:
        return 2
    guess = n+1
    if guess % 2 == 0:
        guess = guess + 1
        
    while not is_prime(guess):
        guess += 2
    return guess

def is_prime(a):
    if a == 2:
        return True
    prime = a %2 != 0  #flag for odds - prime is TRUE if odd
    divisor = 3
    lim = math.sqrt(a) #checks up to square root of number
    while (divisor <= lim) and prime:
        prime = a%divisor !=0 # flag for primality
        divisor += 2 #move on to the next odd
        
    return prime

def print_num_primes_starting_from(num, start):
    if num == 0:
        print("Request was for 0 primes")
    else:
        print('First',num,'primes after', start, '.')
        current = start
        for i in range(num):
            current = get_next_prime(current)
            print((i+1), current)
            
#print_num_primes_starting_from(10, 7)
            
## Define a function called is_a_party(a,p), where a is
## the number of apples and p is the number of pies
## we throw a party if a is more than  5 and p are more than 10
            
def is_a_party(a,p):
    if a>5 and p>10:
        return True
    else:
        return False
    
# a function with zero parameters
def throw_party():
    num_apples = int(input("How many apples do you have?"))
    num_pies = int(input("How many pies do you have?"))
    
    if is_a_party(p = num_pies, a = num_apples):
        return "EY, let's party down! "
    else:
        return "7-11 time."
    
print(throw_party())
