# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum): 
            if root is None:
                return False

            sum = sum + root.val

            if root.left is None and root.right is None:
                return sum == targetSum
            
            return dfs(root.left, sum) or dfs(root.right, sum)
        return dfs(root, 0)