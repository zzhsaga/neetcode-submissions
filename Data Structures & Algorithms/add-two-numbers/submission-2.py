# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # one way is we start from the tail of the list, work backward. which requires 
        # carrying if result great than 10

        # another we can do is find exact two number, get the sum, then turn it into a LL 
        # this might not be as elegant as the first one, but easy to do and debug
        dummy = ListNode()
        prev = dummy
        carry = 0
        while l1 or l2 or carry:
            sumi = carry
            sumi += l1.val if l1 else 0
            sumi += l2.val if l2 else 0
            if sumi >= 10:
                sumi = sumi%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sumi)
            prev.next = new_node
            prev = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        
        return dummy.next

