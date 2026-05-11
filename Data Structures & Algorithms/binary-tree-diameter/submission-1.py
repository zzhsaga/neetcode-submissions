# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we might use an iteration appraoch for dfs instead of using call stack
        # using iteration have a problem is, recursion can pass information from child to parent in really straightforward way
        # iteration we might need to use extra memo structure to record them
        # then when we pop curr node, we can check the information from left and right child
        # two information we need to store, 1, left longerst path and right longest path
        # one thing we need to care is when init, instead of empty, we need to set {None:0}
        diameter = 0
        stack = [root]
        finished = {None:0}

        while stack:
            curr = stack[-1]
            

            if curr.left and curr.left not in finished:
                stack.append(curr.left)
            elif curr.right and curr.right not in finished:
                stack.append(curr.right)
            else:
                curr = stack.pop()

                l = finished[curr.left]
                r = finished[curr.right]
                # print(curr.val,l+r)
                diameter = max(l+r,diameter)
                finished[curr] = 1+max(l,r)
        return diameter


        # we can decompose this problem into, the longest path I can get from right + the longest path from the left would be the longest path of current node
        # then we recursively handle this 
        # but I think we should maintain a global varaible because it has two senario
        # 1. the final diameter use one of curr child, 
        # 2. the final diameter use both children
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.diameter = max(self.diameter, l+r)
            return 1 + max(l,r)
        
        dfs(root)
        return self.diameter
        # do we have any way to improve this?
        # I think retrival every node is nessasary, then is there any way we can prune the tree or do less calculation?
        # I dont think there is any straight forward anwser

        # how about bfs, dfs is easier for me since it can decompose the big problem into smaller one, espeically for each node, exactly two information we need, two output we need to provide
        # bfs is harder because we expect passing information along the process, but think of the leftmost and right most node, they need to know they have a common parent as root, I am not sure there is any trival solusion on this
        # I am thinking about make a hashmap, but feels like we have to update all the prev nodes when we reach a new node....probably this is no how this work