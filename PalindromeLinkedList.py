# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr1 = []
        current = head
        while current:
            arr1.append(current.val)
            current = current.next
        return arr1 == arr1[-1::-1]
