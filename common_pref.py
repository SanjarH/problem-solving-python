# Learn Python together
"""Write a function to find the longest common prefix string amongst an array of strings.
Input: strs = ["flower","flow","flight"]
Output: "fl" 
"""
# Solution
def longestCommonPrefix(strs):
    if not strs: # return empty str if input is empty str
        return ""
    output = "" # empty output
    shortest_str = min(strs, key=len) # get the shortest string in the list 
    for i in range(len(shortest_str)): # check each characters of the shortest string 
        if all(s[i] == shortest_str[i] for s in strs): # check if every string have the same character at index i 
            output += shortest_str[i]     # add character to output 
        else:
            break               # otherwise return empty output
    return output
# Check
strs = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["ab", "a"]
print(longestCommonPrefix(strs)) # Output: ->  fl
print(longestCommonPrefix(strs2)) # Output: -> 
print(longestCommonPrefix(strs3)) # Output: ->  a