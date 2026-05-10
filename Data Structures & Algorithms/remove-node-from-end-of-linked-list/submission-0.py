# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # turn this into a list will be easiest
        nodeList = []
        start = head
        while head:
            nodeList.append(head)
            head = head.next
        if len(nodeList) == 1:
            return None
        target_index = len(nodeList) - n
        if target_index == 0:
            start = nodeList[1]
        elif target_index == len(nodeList) - 1:
            nodeList[-2].next = None
        else:
            nodeList[target_index-1].next = nodeList[target_index+1]
        
        return start