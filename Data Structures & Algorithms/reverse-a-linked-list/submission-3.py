# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head 
        if head is None:
            return None 
            
        # How do we iterate through linked list nodes: 
        # start with head node : 
        node = head
        prev = None
        while node is not None:
            

            next_node = node.next # saving the address to next node, before any update 
            node.next = prev  
            prev = node

            node = next_node
            if (node is None):
                head = prev

        return head