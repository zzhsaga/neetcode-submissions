# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # one way to do this is retrival two trees simuteniously, 
        # None handling is a thing
        # if both None or both valid, return True, else return False
        # if both valid
        # we want to make sure the left child are the same, the right child are the same, and curr p and q are same in val
        if not p or not q:
            return p is q 


        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)  
        