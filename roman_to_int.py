# Learn Python together

""" Given a roman numeral, convert it to an integer.
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
"""            
# Solution

def romanToInt(s):
    #create dictionary with romans numerals as a key and integers as a value
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # output 
    result = 0
    # use for loop for chcecking characters in range of lenths a string - s
    for i in range(len(s)):
        #check if chararter in s(string) is > 0 and is second charecter greater then previous character 
         # if yes, subtract 2 times the value of the previous character and add to result
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
            result += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
        else:
            # if second character less then previous character add it to result
            result += roman_dict[s[i]]
    return result
# check
print(romanToInt('MCMXCIV')) # output -> 1994
print(romanToInt('DCIX')) # output -> 609

# Solution 2 
def romanToInt2(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in s[::-1]:
        curr_value = roman_dict[c]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value
    return result

print(romanToInt2('MMMCMXCIX')) # output -> 1994
print(romanToInt2('DCIX')) # output -> 609