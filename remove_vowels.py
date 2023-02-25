# Learn Python together
'''Function for removing vowels in Python'''

# Solution
def disemvowel(string_):
    new_string = ''
    for char in string_:
        if char not in "aeiouAEIOU":
            new_string += char 
    return new_string  

# check 
print(disemvowel('removing vowels')) 
# output -> rmvng vwls