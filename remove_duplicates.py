# Learn Python together

'''Given an integer array nums sorted in non-decreasing order, remove 
the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.'''

# Solution
def removeDuplicates(nums):
    if not nums:
        return 0
    k = 0 
    for i in range(len(nums)):
        # check if the current value isn't equal to the value at index k 
        if nums[i] != nums[k]:
            k += 1 
            # update the element at index k to be the current element
            nums[k] = nums[i] 
    return k + 1 # return the count of unique elements

list1 = [0,0,1,1,1,2,2,3,3,4]
list2 = [1,1,2,]
list3 = []
print(removeDuplicates(list1)) # Output -> 5
print(removeDuplicates(list3)) # Output -> 0
print(removeDuplicates(list2)) # Output -> 2


