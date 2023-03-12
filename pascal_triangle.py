# Learn Python together
"""Given an integer numRows, return the first numRows of Pascal's triangle"""

# Solution
def pascals_triangle(num):
    # define the first row of Pascals Triangle
    result = [[1]]
    # iteretion from the second row to num
    for i in range(1, num):
        # create row variable with first element of current row which is always 1
        row = [1]
        # iteratation from 1 to i for generating middle elements of current row
        for j in range(1, i):
            # adding to current row sum of two adjacent elemnts in the previous row
            row.append(result[i-1][j-1] + result[i-1][j])
        # adding the last element of the current row which is always 1
        row.append(1)
        # adding all of the rows to result - triangle list
        result.append(row)
    return result
        
# check     
print(pascals_triangle(5)) 
# -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(pascals_triangle(1)) 
# -> [[1]]
print(pascals_triangle(6)) 
# -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
