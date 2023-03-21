# Learn Python together
"""Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0."""

# Solution 1 for 32-bit integers 
def reverse_number(x):
    pos = 1
    if x < 0:
        # negating the input number if its negative and store in pos
        pos = -1
        x = -x 
    # converting number to str and reverse it   
    reverse = int(str(x)[::-1])
    # return reverse if its 32 bit integer
    return pos * reverse if reverse <= 2**31 - 1 else 0   
    
# check            
print(reverse_number(321)) # -> 123
print(reverse_number(-567)) # -> -765
print(reverse_number(2585645646453)) # -> 0
print(reverse_number(-2585645646453)) # -> 0

# Solution 2 for 64-bit integers
def reverse_number2(x):
   # for negative inputs
    pos = 1
    if x < 0:
        # negating the input number if its negative and store in pos
        pos = -1
        x = -x
    reverse = 0  
    # use a while loop for interation
    while x > 0:
        # getting last digit of x  
        pop = x % 10
        # use floor division for droping last digit
        x //= 10  
        # multipe the previous reversed digits by 10 and add th current digit
        reverse = reverse * 10 + pop
    # return multiplied reversed num by pos
    return reverse * pos
# check       
print(reverse_number2(321)) # -> 123
print(reverse_number2(-567)) # -> -765
print(reverse_number2(2585645646453)) # -> 3546465465852
print(reverse_number2(-2585645646453)) # -> -3546465465852



            
        
    