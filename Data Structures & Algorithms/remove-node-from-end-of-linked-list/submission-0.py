# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Two-pointer approach will be that as i need : two updates on adjacent elements 
        # 1, 2, 3, 4, -- : update on 2 , and 4 directly -- which means i = 2 , j = 4 ( 1,3 )
        # difference of two positions in index : 

        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head
        for i in range(1,n+1):
            right = right.next 
        
        while right:
                
            left = left.next
            right = right.next 
        
        right_dirt = left.next.next 
        left.next = right_dirt

        return dummy.next        

