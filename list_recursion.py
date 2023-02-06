""" Write a Python program of recursion list sum. 
    Test Data: [1, 2, [3,4], [5,6]]
    Expected Result: 21 """
    
# Solution 1   
def recurs_list(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count += recurs_list(i) # recursive - calling a function within itself 
        else:
            count += i
    return count
# check
test_data = [1, 2, [3,4], [5,6]]
print(recurs_list(test_data)) # Output -> 21

# Solution 2 using reduce function
from functools import reduce 
"""The reduce function is used to compute a single value from a sequence by 
successively combining elements using a binary function and an optional initial value."""

def recurs_list2(lst): # used functions lambda for sum items, isinstance for cheking type of y is a list   
    return reduce(lambda x, y: x + recurs_list2(y) 
                  if isinstance(y, list) else x + y, lst, 0) # 0 used as an optional initial value.
# check
print(recurs_list2(test_data)) # Output -> 21
