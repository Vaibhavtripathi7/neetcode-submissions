# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, max_val, min_val):
            if root is None: 
                return True
            # How do we update the values : for left child , max val
            # for right child, its: min val 
            # Just have to manage the root-case
            if (root.val >= max_val or root.val <= min_val):
                return False 
            return dfs(root.left, root.val, min_val) and dfs(root.right, max_val, root.val)      
            # have to pass down the values for 
        return dfs(root, float('inf'), float('-inf'))



