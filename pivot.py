# Learn Python together

"""Given an array of integers nums, 
calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers
strictly to the left of the index is equal to the sum of all 
the numbers strictly to the index's right."""

# Solution 1

def pivotIndex1(nums) -> int:
    pivot = 0
    # getting sum of the numbers from left side of the pivot
    left_sum = sum(nums[:pivot])
    # getting sum of the numbers from fight side of the  pivot
    right_sum = sum(nums[pivot+1:])
    
    # lopping through the list
    for _ in range(len(nums)-1):
        if left_sum == right_sum:
            # if sums are equal, return the pivot index
            return pivot  
        else:
            # otherwise left sum += pivot index, 
            # right sum -= pivot index+1
            left_sum += nums[pivot] 
            right_sum -= nums[pivot+1] 
            pivot += 1
    # if the sums still not equal, return -1
    if left_sum == right_sum:
        return pivot
    else:
        return -1


# Solution 2
def pivotIndex2(nums) -> int:
    left_sum = 0
    # sum of all numbers
    right_sum = sum(nums)

    for i in range(len(nums)):
        # substract the current num from right sum
        right_sum -= nums[i] 
        # return index if sums are equal
        if left_sum == right_sum:
            return i
        # adding current num to the left sum
        left_sum += nums[i] 
    # if there isn't pivot, -1    
    return -1
        

# Solution 3
def pivotIndex3(nums) -> int:
    left_sum = 0
    # sum of all numbers
    right_sum = sum(nums)

    for i, num in enumerate(nums):
        # if sums are equal, return index
        if left_sum == right_sum -left_sum - num:
            return i
        # add current num to the left sum
        left_sum += nums[i] 
    # if there isn't pivot, -1
    return -1
        
# check         
nums = [1,7,3,6,5,6]
nums2 = [1,7]
print(pivotIndex1(nums)) # Output-> 3
print(pivotIndex2(nums)) # Output-> 3
print(pivotIndex3(nums)) # Output-> 3

print(pivotIndex1(nums2)) # Output-> -1
print(pivotIndex2(nums2)) # Output-> -1
print(pivotIndex3(nums2)) # Output-> -1

# Check time 
import timeit

t1 = timeit.timeit(lambda: pivotIndex1(nums), number=10000)
print("pivotIndex1 execution time:", t1) # -> 0.011717599999999995

t2 = timeit.timeit(lambda: pivotIndex2(nums), number=100000)
print("pivotIndex2 execution time:", t2) # -> 0.08669160000000001

t3 = timeit.timeit(lambda: pivotIndex3(nums), number=100000)
print("pivotIndex3 execution time:", t3) # -> 0.09343009999999999

