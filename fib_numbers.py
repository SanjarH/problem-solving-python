# Learn Python together

""" Write a function to calculate the Fibonacci numbers.
- Fibonacci numbers commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of
the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1. """

# importing lru_cache function for memoization
from functools import lru_cache 
# Solution
@lru_cache(maxsize=None) 
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1                     
    return fibonacci(n-1) + fibonacci(n-2) # recursive case 
           
# Check    
print(fibonacci(42)) # Output -> 267914296
print(fibonacci(12)) # Output -> 144
print(fibonacci(-11)) # Output -> 0
print(fibonacci(6)) # Output -> 8

# Solution 2 from LinkednIn folowers
def fibonacci2(n):
  i = 0
  previous, current = 0, 1
  while i < n:
    previous, current = current, previous + current
    i += 1
  return previous

print(fibonacci2(42))
print(fibonacci2(12)) # Output -> 144
print(fibonacci2(-11)) # Output -> 0
print(fibonacci2(6)) # Output -> 8

