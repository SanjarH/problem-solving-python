from __future__ import  division
# Learn Python together
""" Write a function that evaluetes the Ackermann funtion"""

# Solution 1 with limited input numbers
def ackermann(m, n):
    if m == 0: 
        return n + 1
    elif m > 0 and n == 0: 
        return ackermann(m - 1, 1)  
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    else:
        return 0

print(ackermann(3,4)) 
# Output -> 125
print(ackermann(3,7)) 
# Output -> RecursionError: maximum recursion depth exceeded in comparison

# Solution 2 using memoization

cache = {} # empty dictionary for storing results

def ackermann_memo(m, n):
    if m == 0:
        return n+1
    
    if n == 0:
        # return recursively function with (m-1,1)
        return ackermann_memo(m-1, 1)
    # If the result of this function call has been previously calculated
    if (m, n) in cache: 
        # return the stored result from the dictionary
        return cache[m, n]  
    else:
        # otherwise return current recusive function result in the dictionary
        cache[m, n] = ackermann_memo(m-1, ackermann_memo(m, n-1))
        return cache[m, n]

# check
print(ackermann_memo(3, 7))
# output-> 1021
print(ackermann_memo(3, 8))
# output-> 2045
print(ackermann_memo(4, 8))
# output-> RecursionError: maximum recursion depth exceeded in comparison
# Do you know why ?