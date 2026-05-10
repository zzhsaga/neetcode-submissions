# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # main iteration part
        # 1. compare both current node, and choose the smaller one
        # 2. prev link to the smaller one, and move current to the next
        # early terminated
        # 1. if one list is exhrausted
        dummy = ListNode()
        prev = dummy

        # if list1.value >= list2.value:
        #     dummy.next = list1
        # else:
        #     dummy.next = list2
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2
        
        return dummy.next
