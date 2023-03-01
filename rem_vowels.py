# Learn Python together

'''Write a Python function that remove vowels'''

# Solution

def remove_vowels(s):
    vowels = "aeiuoAEIOU"
    output = ''
    for char in s:
        if char not in vowels:
            output += char
    return output

# check
print(remove_vowels('Python is the best'))
# thanks for your time, if you like it share and comment:)