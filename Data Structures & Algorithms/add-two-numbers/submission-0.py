# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # one way is we start from the tail of the list, work backward. which requires 
        # 1. recursion
        # 2. passing value in each step

        # another we can do is find exact two number, get the sum, then turn it into a LL 
        # this might not be as elegant as the first one, but easy to do and debug
        
        sumi = 0
        for start in [l1,l2]:
            base = 1
            while start:
                curr = start.val*base
                base = base*10
                sumi += curr
                start = start.next
        sumi_list = str(sumi)[::-1]

        head = ListNode()
        curr = head

        for s in sumi_list:
            new_node = ListNode(int(s))
            curr.next = new_node
            curr = new_node
        
        return head.next

