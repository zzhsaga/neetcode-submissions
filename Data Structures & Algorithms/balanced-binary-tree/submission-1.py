# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we need to retrival all the leaves and track their depth/height
        # for every node, check the left high and right high
        # onething is, if one false happen, we should be able to propagate it to root or we use a global varable
        # I am thinking about if there is a way we dont need to have a helper function
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == -1 or r== -1 or abs(l-r) > 1:
                return -1
            else:
                return 1 + max(l,r)

        result = dfs(root)
        # print(result)
        if result == -1:
            return False
        else:
            return True          
            
        
            