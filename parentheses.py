# Learn Python together
"""Write a python program to check parentheses is valid or not"""

# Solution 1 using for loop, append and pop methods
def isValid(strs):
    open_parenth = ["(", "[", "{"]
    close_parenth = [')', ']', "}" ]
    stack = []

    for char in strs:
        if char in open_parenth:
            stack.append(char)
        elif char in close_parenth:
        # check if empty stack or if the last item in the stack matches the current char 
            if not stack or open_parenth.index(stack[-1]) != close_parenth.index(char):  
                return False
            stack.pop() # pop method used for removing the last char
    return not stack  
# check       
print(isValid("()[]{")) # False
print(isValid("()[]{}")) # True

# Solution 2 using while loop, any and replace methods
def isValid2(strs):
    list_parentheses = ["[]", "()", "{}"]
    # iteration for any chars in strs and list and check if they are matched
    while any(char in strs for char in list_parentheses):
        for par in list_parentheses:
            strs = strs.replace(par, "") # if are matched remove last char
    return not strs
# check     
print(isValid2("()[]{")) # False
print(isValid2("()[]{}")) # True