# Learn Python together
""" Write a function that converts integer to roman numerical"""

# Solution
def int_to_roman(num: int) -> str:
    # create the list with tuples representing the romans and their values 
    roman_map = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
        ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
        ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    if num <= 0:
            return "Roman numerals don't represent 0 or negative numbers"
    # epmty result
    result = ''
    # using for loop for iterate over the roman_map list:
    for roman, value in roman_map:
        # while loop runs until the value of the current roman is greater than the num   
        while value <= num:
            result += roman # For each iteration of the while loop, the roman is added to the result
            num -= value    # and the value is subtracted from num
    return result

# check
print(int_to_roman(1994)) # output -> MCMXCIV
print(int_to_roman(-609)) # output -> Roman numerals don't represent 0 or negative numbers
print(int_to_roman(0)) # output -> Roman numerals don't represent 0 or negative numbers
print(int_to_roman(609)) # output -> DCIX