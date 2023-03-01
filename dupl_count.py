# Learn Python together

"""Write a function that will return the count of distinct 
case-insensitive alphabetic charactersand numeric digits 
that occur more than once in the input string."""

# Solution

def duplicate_count(text):
    # convert text to lowecase
    text = text.lower()
    
    # using a set comprehesion to get a set of chars 
    duplicates = {char for char in text if text.count(char) > 1}
    
    return len(duplicates)

# check

print(duplicate_count('Abcdaa'))
print(duplicate_count('PythonnnssDD!!'))