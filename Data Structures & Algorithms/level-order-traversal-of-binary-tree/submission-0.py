# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this natraully fit with BFS
        # using a for loop to batch pop/add  nodes for the same level

        if not root:
            return []
        level_order_list = []
        deq = deque([root])

        while deq:
            single_level_list = []
            for _ in range(len(deq)):
                curr = deq.popleft()
                single_level_list.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
            level_order_list.append(single_level_list)

        
        return level_order_list


