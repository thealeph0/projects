import matplotlib.pyplot as plt

def pascals_triangle(n): #n is the number of rows
    triangle_str = "" 
    for i in range(n):
        triangle_str += (" " * (n-i)) #printing leading spaces for formatting
        
        coefficient = 1
        
        for j in range(i+1):
            triangle_str += str(coefficient) + " "
            coefficient = coefficient * (i-j) // (j+1)
            
        triangle_str += "\n" # move to the next line after each row
    return triangle_str

# print(pascals_triangle(4))
        
def drawn_triangle(n):
    tri = pascals_triangle(n)
    rows = tri.strip().split('\n') #removed whitespace and split by each \n
    
    for i, row in enumerate(rows):
        coeffs = row.strip().split() #removes whitespace and splits per character
        for j, coeff in enumerate(coeffs):
            if (int(coeff) % 2 == 1):
                color = 'blue'
            
            else:
                color = 'black'
            plt.text(j-i/2, -i, coeff, ha='center', va='center')
    
    plt.xlim(-n/2,n/2)
    plt.ylim(-n,1)
    plt.axis('off')
    
    plt.show()
    
drawn_triangle(5)