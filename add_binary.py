# Learn Python together

"""Given two binary strings a and b, 
return their sum as a binary string."""

# Solution 
# we can use bin function and change types
def addBinary(a:str, b:str) -> str:
    return str(bin(int(a, 2) + int(b, 2)))[2:]
            
# check    
print(addBinary("1010",'1011')) # Output -> 10101
print(addBinary('0','0')) # Output -> 0
print(addBinary('0','1')) # Output -> 1


def addBinary2(a:str, b:str) -> str:
    
    carryover = 0
    result = ""

    # using for loop and max function to iterate 
    # through the strings starting from the last index
    for i in range(max(len(a), len(b))): 

        # geting the numbers at the current index of each string, or 0 if beyond the limit
        a_num = int(a[::-1][i]) if i < len(a) else 0
        b_num = int(b[::-1][i]) if i < len(b) else 0

        # sum of numbers and carryover
        total = a_num + b_num + carryover

        # result would be the rest of total divided by 2 + result that was before 
        result = str(total % 2) + result

        # carryover is 1 if total is greater than 1, otherwise 0 
        carryover = 1 if total > 1 else 0

    # add any remaining carryover to the beginning of result 
    if carryover == 1: 
        result = "1" + result 

    return result

# check
print(addBinary2("1010",'1011')) # Output -> 10101
print(addBinary2('0','0')) # Output -> 0
print(addBinary2('0','1')) # Output -> 1
