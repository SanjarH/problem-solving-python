# Learn Python together

"""Given a non-empty array of integers nums, 
every element appears twice except for one.
Find that single one."""

# Solution

def single_number(nums):
    # use dictionary comprehension to count nums
    count = {num: nums.count(num) for num in nums}
    # return minimum if nums 
    return min(count, key=count.get)

#check 

nums = [1, 2, 2, 3, 3]
nums2 = [4, 3, 3, 2, 2]
nums3 = [5]

print(single_number(nums)) # -> Output 1
print(single_number(nums2)) # -> Output 4
print(single_number(nums3)) # -> Output 5

