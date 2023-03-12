# Learn Python together
"""Given an integer columnNumber, return its corresponding 
column title as it appears in an Excel sheet."""
# Solution
def convert_to_title(colNum):
    result = ""
    while colNum > 0:
        # getting a zero-based index
        colNum -= 1
        # using divmod function to get quotient and remainder 
        quotient, remainder = divmod(colNum, 26)
        # converting the remainder to a character using the 
        # ASCII code and addin the result
        result = chr(remainder + 65) + result
        # setting index of the next wrap to colNum
        colNum = quotient
    return result

# check            
print(convert_to_title(2))  
print(convert_to_title(26))           
print(convert_to_title(-1))
print(convert_to_title(101))
print(convert_to_title(450))