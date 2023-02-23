# Learn Python together
'''Given two strings s and t, return true 
if s is a subsequence of t, or false otherwise.
'''
# Solution

def isSubsequence(s: str, t: str) -> bool:
    index = 0
    # check if the index is less then length of s and 
    for letter in t: # the letter in s is equel to the letter in t   
        if index < len(s) and s[index] == letter:
            index += 1    
    return index == len(s) 

# check    
print(isSubsequence('ace', 'abcde')) # Output -> True
print(isSubsequence("axc", "ahbgdc")) # Output -> False
print(isSubsequence("ab", 'baab')) # Output -> True