# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root): 

            if root is None: 
                return

            queue = deque()
            queue.append(root)

            while queue:
                z = len(queue)
                local = []
                for i in range(z):
                    node = queue.popleft() 
                    local.append(node.val)
                    print(node)
                    if node.left: 
                        queue.append(node.left)
                    if node.right: 
                        queue.append(node.right)

                res.append(local)
        bfs(root)
        return res 