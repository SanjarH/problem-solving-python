# Learn Python together

""" Write a function to calculate the Fibonacci numbers.
- Fibonacci numbers commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of
the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1. """

# Solution
def fibonacci(n):    
    if n <= 0:
        return 0
    elif n == 1:
        return 1                     
    return fibonacci(n-1) + fibonacci(n-2) # recursive case 
           
# Check    
print(fibonacci(5)) # Output -> 5
print(fibonacci(12)) # Output -> 144
print(fibonacci(-11)) # Output -> 0
