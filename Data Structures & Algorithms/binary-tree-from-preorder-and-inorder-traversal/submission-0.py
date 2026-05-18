# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # i do remember for inorder list, the left and right order is exactly like the position relation on tree
        # but preorder, I am not sure, I think the k nodes that follow each node, it is the subtree of it
        # so in theory, we can use divide and conque, from the 1, find its boudary in the inorder, then find two seperate part in the preorder, keep this util the size of tree is 1, so we build the node, return to upper level
        # but the index handling is too complicated
        def build(root,l,r):
           
            preorder_index = preorder.index(inorder[root])
            print(root,l,r,preorder_index)
            left_size = root - l
            right_size = r - root
            print(left_size,right_size)
            if left_size:
                left_index = inorder.index(preorder[preorder_index + 1])
                left = build(left_index, l,root-1)
            else:
                left = None
            if right_size:
                right_index = inorder.index(preorder[preorder_index + 1 + left_size])
                right = build(right_index, root + 1,r)
            else:
                right = None
            return TreeNode(inorder[root],left,right)

        
        return build(inorder.index(preorder[0]),0,len(inorder)-1)
