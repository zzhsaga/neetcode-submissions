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
        # prev = ListNode()
        while l < r:
            # prev.next = nodeList[l]
            nodeList[l].next = nodeList[r]
            l += 1
            if l >= r:
                break
            nodeList[r].next = nodeList[l]
            r -= 1 
        
        nodeList[l].next = None
        # this is turn LL into list, then use pure list logic to handle
        # if there is no extra list allow, probably we can use recursion but would be difficult

