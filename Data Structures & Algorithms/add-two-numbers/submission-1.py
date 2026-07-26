# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer approach : with each and every next : we sum and create a new node and connect them 
        first = l1 
        second = l2  
        save_node = ListNode(0) # this will be the head node
        head = save_node
        carry = 0
        while (first is not None or second is not None or carry > 0):
            
            val1 = first.val if first else 0
            val2 = second.val if second else 0
            sumof = val1 + val2 + carry

            carry = sumof // 10
            node_val = sumof % 10

            new_node = ListNode(node_val) 
            save_node.next = new_node
            save_node = new_node

            if (first is not None):
                first = first.next 
            if (second is not None):
                second = second.next 
        return head.next