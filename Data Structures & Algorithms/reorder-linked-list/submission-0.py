# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we can recusively travel to n - 1 
        # one pointer go forward, one pointer go backward
        # store all the nodes in a list will be straightfoward

        nodeList = []
        while head:
            nodeList.append(head)
            head = head.next
        
        l = 0
        r = len(nodeList) - 1
        # we dont want any duplication, so 
        dummy = prev = ListNode()
        while l < r:
            prev.next = nodeList[l]
            nodeList[l].next = nodeList[r]
            prev = nodeList[r]
            l += 1
            r -= 1 
        if l == r:
            prev.next = nodeList[l]
            prev = nodeList[l]
        prev.next = None


