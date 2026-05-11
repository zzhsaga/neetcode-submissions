# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we can decompose this problem into, the longest path I can get from right + the longest path from the left would be the longest path of current node
        # then we recursively handle this 
        # but I think we should maintain a global varaible because it has two senario
        # 1. the final diameter use one of curr child, 
        # 2. the final diameter use both children
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.diameter = max(self.diameter, l+r)
            return 1 + max(l,r)
        
        dfs(root)
        return self.diameter