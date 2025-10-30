##Function computes the matrix product (also called matrix multiplication) between two 2D lists

def dot_product(list1,list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be the same length")
    
    product = 0
    
    for i in range(len(list1)):
        product += list1[i] * list2[i]
    
    return product

def matrix_multi(matrix1,matrix2):
    row_m1 = len(matrix1)
    col_m1 = len(matrix1[0])
    row_m2 = len(matrix2)
    col_m2 = len(matrix2[0])
    
    #ensure sizes match for multiplication
    if col_m1 != row_m2:
        raise ValueError("Number of columns in matrix1 must match rows in matrix 2.")
    
    #empty matrix of the correct size
    matrix = [
        [0]*col_m2 for _ in range(row_m1)]
    
    for i in range(row_m1):
        for j in range(col_m2):
            for k in range(col_m1):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                ##matrix[i][j] = dot_product(matrix1[i], [row[j] for row in matrix2]) ##alternate using dot_product method
                
    return matrix
            
    