# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using BFS will be straight forward, we do a level pop then we can collect the last nodes for each level
        # one optimal approach I am thinking of is in each level, the rightmost node always come from the right most node in prev level, the worst case might be the same but 
        # this is not right logic, if th prev right most node doesnt have child, then it will break and skip the rest of tree, so probably there si no straightfoward optimization
        # for DFS, since in each node, we lack of level awareness, so it would be hard to do
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
