"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #how do create a copy : linked-list -- first important thing : 
        # will have to iterate to every node: to create a new node: which points to this: 
        if head is None:
            return 

        node = head
        dict_ = {}

        while node: 
            dict_[node] = Node(node.val)
            node = node.next

        node = head

        while node:
            new_node = dict_[node]
            if (node.next is None):
                new_node.next = None

            else: new_node.next = dict_[node.next]
            
            if(node.random) is None:
                new_node.random = None
        
            else: new_node.random = dict_[node.random]
            node = node.next 
        
        return dict_[head]
         


