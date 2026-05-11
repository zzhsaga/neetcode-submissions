# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # this we can use bfs
        deq = deque([p,q])

        while deq:
            curr_p = deq.popleft()
            curr_q = deq.popleft()
            if not curr_p or not curr_q:
                if curr_p is curr_q:
                    continue
                else:
                    return False
            # print(curr_p,curr_q)
            if curr_p.val != curr_q.val:
                return False
            deq.append(curr_p.left)
            deq.append(curr_q.left)
            deq.append(curr_p.right)
            deq.append(curr_q.right)
        
        return True
        # one way to do this is retrival two trees simuteniously, 
        # None handling is a thing
        # if both None or both valid, return True, else return False
        # if both valid
        # we want to make sure the left child are the same, the right child are the same, and curr p and q are same in val
        if not p or not q:
            return p is q 


        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)  
        