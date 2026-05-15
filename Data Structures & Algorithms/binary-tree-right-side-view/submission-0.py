# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using BFS will be straight forward, we do a level pop then we can collect the last nodes for each level
        # one optimal approach I am thinking of is from the 

        right_side_view_list = []
        if not root:
            return right_side_view_list
        
        deq = deque([root])

        while deq:
            level_len = len(deq)
            for i in range(level_len):
                curr = deq.popleft()
                if i == level_len - 1:
                    right_side_view_list.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
        
        return right_side_view_list
