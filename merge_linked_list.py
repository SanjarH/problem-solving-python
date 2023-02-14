# Learn Python together
"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list."""

# Solution
# import Optional type
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
         
        if not list1 or not list2: # If one of the lists is empty,
            return list1 or list2  # return the other list 
        # comparing lists values for getting lower value
        if list1.val < list2.val:
            # lover value from list1
            head = list1
            # using recursive get other values in tail variable
            tail = self.mergeTwoLists(list1.next, list2)
        else: # if the value of second node is lower than first node
            # lover value from list2
            head = list2
            # using recursive get other values in tail variable
            tail = self.mergeTwoLists(list1, list2.next)
        #  connects the head node and the tail node of the merged linked list
        head.next = tail
        return head # return current node

#check    
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
result = solution.mergeTwoLists(list1, list2)
expected_result = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

# funtion to printing linked-list result
def print_list(head):
    node = head
    while node:
        # print current value and '->' if there is a next value in linked-list else empty string
        print(node.val, end=" -> " if node.next else "")
        # moving to next value
        node = node.next 
    print()

print_list(result) 
# Output -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
print_list(expected_result)
# Output -> 1 -> 1 -> 2 -> 3 -> 4 -> 4

