# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # fast and slow pointers : logic is if there is a cycle -- fast pointer will meet or cross the 
        # slow pointer in iterations
        # fast and slow : can start at same point : just update in fast is bigger 
        # and eventually they will be equal at some point ! 

        fast = head 
        slow = head 
        
        while fast and fast.next: # both check so we don't get attribute error on : fast.next.next

            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True 

        return False            