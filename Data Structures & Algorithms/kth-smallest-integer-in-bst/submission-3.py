# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # finding k smallest in a bst
        # bst gives us extra leverage that it is monotonic for in order dfs, 
        # so we can have track the progress, update between left and right child, and a global ans value to carray the anwser
        self.k_smallest = -1
        self.k = k
        self.count = 0

        def dfs(root):
            if not root or self.k_smallest != -1:
                return 
            
            dfs(root.left)
            self.count += 1
            print(root.val,self.count)
            if self.count == self.k:
                self.k_smallest = root.val
            
            dfs(root.right)

            return 
        
        dfs(root)
        return self.k_smallest
