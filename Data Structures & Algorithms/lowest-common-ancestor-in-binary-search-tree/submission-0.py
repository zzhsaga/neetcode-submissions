# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use dfs, the first node receive two positive signals are the ancestor
        self.ans = -1

        def dfs(root,p,q):
            if not root or self.ans != -1:
                return 0
            
            l = dfs(root.left,p,q)
            r = dfs(root.right,p,q)
            count = l + r
            if root.val == p.val or root.val == q.val:
                print('root check functioning')
                count += 1
            print(count)
            if count == 2 and self.ans == -1:
                self.ans = root
            
            return count
        dfs(root,p,q)
        return self.ans