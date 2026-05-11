# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subtree valid means 
        # 1. the subRoot exist in the tree as node_1
        # 2. subRoot and node_1 have exactly same chidren

        # so we can first find the node, then check if the children are the same
        def is_same(p,q):
            if not p or not q:
                return p is q
            
            return p.val == q.val and is_same(p.left,q.left) and is_same(p.right,q.right)
        deq = deque([root])

        while deq:
            curr = deq.popleft()
            if curr.val == subRoot.val:
                if is_same(curr,subRoot):
                    return True
            if curr.left:
                deq.append(curr.left)
            if curr.right:
                deq.append(curr.right)
        
        return False

        



        