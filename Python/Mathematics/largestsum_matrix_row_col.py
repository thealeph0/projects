def row_with_largest_sum(data):
    # Initialize variables to track the largest sum and the corresponding row index
    max_sum = float('-inf')
    max_index = -1
    
    # Loop through each row and its index
    for i, row in enumerate(data):
        row_sum = sum(row)  # Calculate the sum of the current row
        
        # If the current row's sum is larger than the max found so far, update max_sum and max_index
        if row_sum > max_sum:
            max_sum = row_sum
            max_index = i
    
    return max_index


def column_with_largest_sum(matrix):
    # Handle edge case where matrix might be empty
    if not matrix or not matrix[0]:
        return -1  # Return -1 if matrix is empty

    # Get the number of columns
    num_cols = len(matrix[0])
    
    # Initialize variables to track the largest sum and the corresponding column index
    max_sum = float('-inf')
    max_index = -1
    
    # Loop through each column index
    for i in range(num_cols):
        # Calculate the sum of the current column
        col_sum = sum(row[i] for row in matrix)
        
        # If the current column's sum is larger than the max found so far, update max_sum and max_index
        if col_sum > max_sum:
            max_sum = col_sum
            max_index = col

    return max_index