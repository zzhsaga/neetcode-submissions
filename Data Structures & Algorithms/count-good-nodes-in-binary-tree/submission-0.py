# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # it wants the historical maximum on the path, the BFS and DFS both work with carrying one extra info

        self.good_nodes_count = 0

        def dfs(root, maxi):
            if not root:
                return 
            if root.val >= maxi:
                maxi = root.val
                self.good_nodes_count += 1
            dfs(root.left,maxi)
            dfs(root.right,maxi)
        dfs(root,root.val)
        return self.good_nodes_count

        