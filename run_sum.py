# Learn Python together

'''Given an array nums. We define a running sum of an array 
as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums. Input: nums = [1,2,3,4]
Output: [1,3,6,10] -> [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]'''

# Solution
def running_sum(nums):
    index = 0
    result = []
    # loping until index is equal to length of nums
    while index < len(nums):
        if index == 0:
            # getting the first number and adding it to the result
            num = nums[0]
            result.append(num)
        else:
            # adding sum of current and previous numbers to the result
            num = nums[index] + result[index-1]
            result.append(num)
        index += 1
    return result
        
# check             
print(running_sum([1,2,3,4])) # Output -> [1, 3, 6, 10]
print(running_sum([3,1,2,10,1])) # Output -> [3, 4, 6, 16, 17]
print(running_sum([1,1,1,1,1])) # Output -> [1, 2, 3, 4, 5]
