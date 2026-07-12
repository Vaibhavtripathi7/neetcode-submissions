class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Store these locally to avoid repeated lookups
        p_val = p.val
        q_val = q.val
        
        curr = root
        while curr:
            curr_val = curr.val # Store this locally per loop
            
            if p_val > curr_val and q_val > curr_val:
                curr = curr.right
            elif p_val < curr_val and q_val < curr_val:
                curr = curr.left
            else:
                return curr