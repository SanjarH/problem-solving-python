# Learn Python together
"""Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""
# Solution 1
def rot13(message):
    result = ''
    for char in message:
        # chek the char is an alphabet
        if char.isalpha():
            # check the char is uppercase
            if char.isupper():
                # convert chars to ASCII code, subtract ASCII code of 'A' (65),add rot13 than take modulo 26,
                # add ASCII code of 'A' back and convert ASCII code to characters and add it to the result
                result += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                # convert chars to ASCII code, subtract ASCII code of 'a' (97),add rot13 than take modulo 26,
                # add ASCII code of 'a' back and convert ASCII code to characters and add it to the result
                result += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            # otherwise add char to the result
            result += char
    return result
            
# check 
print(rot13('test')) # Output -> grfg
print(rot13('Test')) # Output -> Grfg
print(rot13('aA bB zZ 1234 *!?%')) # Output ->  nN oO mM 1234 *!?%       
        
# Solution 2 using the encode method 
import codecs
def rot13_encode(message):
    return codecs.encode(message, 'rot13')       

# check       
print(rot13_encode('test')) # Output -> grfg  
print(rot13_encode('Test')) # Output -> grfg  
print(rot13_encode('aA bB zZ 1234 *!?%')) # Output -> nN oO mM 1234 *!?%
