# Learn Python together
""" Given an array nums of distinct integers, return all the possible permutations. """

# Solution 1 using loop and recursive

def permute(nums):
    if len(nums)<=1:
        return [nums]
    result= [] # empty list
    # iteration through each item in the list
    for i in range(len(nums)):
        lis = nums[i]  # giving value at index i in lis variable
        new_list = nums[:i]+nums[i+1:] # giving in new list all elemts of the list exclude lis
        for perm in permute(new_list): # recursive call function for creating permutation
            result.append([lis]+perm) # add variables to result
    return result

#check 
list1 = [1,2,3]
list2 = [0]
print(permute(list1)) 
# Output -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permute(list2))
# Output -> [[0]]


# Solution 2 using itertools library with tuples in the list
from itertools import permutations

def perm_tools(nums):
    return list(permutations(nums))

# check
print(perm_tools(list1))
# Output -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(perm_tools(list2))
# Output -> [(0,)]