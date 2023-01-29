# Learn Python together
"""Write a Python program that accept a list of integers
and check the length and the fifth element. Return true 
if the length of the list is 8 and fifth element occurs 
thrice in the said list"""
# solution
def check_num(lst):
    return len(lst) == 8 and list.count(lst[4]) == 3
   
list = [19,19,15,5,5,5,1,2]
print(check_num(list))
# Output -> True

list2 = [19, 15, 5, 7, 5, 5, 2]
print(check_num(list2))
# Output -> False
