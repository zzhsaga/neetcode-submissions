# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for each node, it has two conditions
        # 1. passing to parent, then we choose the sumi that greater than zero
        # 2. as parent so sum from right and left
        self.ans = -1001

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(l+r+root.val,self.ans)
            passing = max(root.val+l, root.val+r)
            return max(passing,0)
        dfs(root)
        return self.ans
        