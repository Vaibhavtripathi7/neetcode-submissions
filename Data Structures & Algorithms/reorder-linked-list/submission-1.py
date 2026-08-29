# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle of the list: using fast and slow pointer:        # Now we have mid node : we need to reverse the list after that node:  
            # Step 1: find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half (AFTER the while loop, not inside it)
        second = slow.next
        slow.next = None  # split the list
        prev = None
        while second:
            save = second.next
            second.next = prev
            prev = second
            second = save
        # now prev is head of reversed second half
        # Step 3: merge alternating
        # your turn — write this part
        prev2 = None 
        while head and prev:
            prev2 = head.next 
            prev3 = prev.next
 
            head.next = prev
            head = prev2
            prev.next = prev2  
            prev = prev3