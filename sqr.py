# Learn Python together

"""Given a non-negative integer x, return the square root of x 
rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""
    
# Solution
import math 
def mySqrt(x):
    if x <= 0:
        return 0
    else:
        return int(math.sqrt(x))
# check    
print(mySqrt(8)) # Output  -> 2
print(mySqrt(-1))# Output -> 0
print(mySqrt(0)) # Output  -> 0
print(mySqrt(999))# Output -> 31

# Solution 2 from LinkedIn follower
def mySqrt2(x):
    a, b = 0, x
    x0 = 0
    while abs(x0*x0 - x) > 0.001:
        x0 = (a + b) / 2
        if x0*x0 > x:
            b = x0
        else:
            a = x0
    return int(x0)

print(mySqrt2(8)) # Output  -> 2
print(mySqrt2(-1))# Output -> 0
print(mySqrt2(0)) # Output  -> 0
print(mySqrt2(999))# Output -> 31

