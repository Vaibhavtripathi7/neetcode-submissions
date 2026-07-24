# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node = head
        # fast and slow pointers : logic is if there is a cycle -- fast pointer will meet or cross the 
        # slow pointer in iterations
        list_ = []
        slow = node
        fast = node.next.next 
        while node is not None:
            if (fast in list_):
                return True
            list_.append(slow)
            slow = node.next
            fast = node.next  
            node = node.next 
        return False