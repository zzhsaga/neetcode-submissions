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
        while l1 and l2:
            sumi = l1.val + l2.val + carry
            if sumi >= 10:
                sumi = sumi%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sumi)
            prev.next = new_node
            prev = new_node
            l1 = l1.next
            l2 = l2.next
        # since we have to handle the last carry instead of directly connect to the rest
        if l1:
            rest = l1
        else:
            rest = l2
        
        while rest:
            sumi = rest.val + carry
            if sumi >= 10:
                sumi = sumi%10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sumi)
            prev.next = new_node
            prev = new_node
            rest = rest.next
        
        if carry:
            new_node = ListNode(1)
            prev.next = new_node
        
        
        return dummy.next

