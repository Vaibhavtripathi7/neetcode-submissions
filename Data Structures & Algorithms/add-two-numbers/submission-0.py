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
        save_node = ListNode(first.val + second.val) # this will be the head node
        head = save_node
        while (first and second) is not None:

            sumof = first.val + second.val
            if ( sumof  >= 10): # let's say sumof = 18 
                # we have to split the nodes and create two nodes : for this case: 
                #create two nodes: and connect them --
                sumofsplit = [int(d) for d in str(sumof)] 
                node1 = ListNode(sumofsplit[1])
                node2 = ListNode(sumofsplit[0])
                node1.next = node2
                save_node.next = node1
                save_node = node2

            else: 
                new_node = ListNode(sumof) # what about it next: same as 
            #now create a new node : starting with head : 
                save_node.next = new_node
                save_node = new_node

            first = first.next 
            second = second.next 
        return head.next