def gcd(a,b):
    if a > b:
        small = b
        large = a
    else:
        small = a
        large = b
    r = large % small #remainder
    print (large, small ,r) #this line adds the current state
    
    while r > 0:
        large = small
        small = r
        r = large%small
        print (large, small ,r)#order matters
        
    return small

print(gcd(234,42))