# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I think traversal order has a special way to handle this but I forgot
        # intuiationally, for each node, we need the maxi of left substree and mini of right subtree
        self.ans = True
        
        def dfs(root):
            if root.left:
                l_mini,l_maxi = dfs(root.left)
                if root.val <= l_maxi:
                    self.ans = False
            else:
                l_mini = l_maxi = root.val
            if root.right:
                r_mini, r_maxi = dfs(root.right)
                if root.val >= r_mini:
                    self.ans = False
            else:
                r_mini = r_maxi = root.val

            
            return l_mini,r_maxi

        dfs(root)

        return self.ans