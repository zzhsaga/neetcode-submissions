"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_map = {}
        dummy = Node(0) # as the prev node of  new LL for returning
        prev = dummy
        start = head

        # create new node
        # store random pointer
        # prev.next = new
        # original pointer move
        # prev pointer move

        # for random pointer persistence
        # we only can garantee we the current new_node exist, but for start.random, we dont know if new_node.random is already created or not
        # then we store a map as old_end -> new_start
        # then when we go throught the LL second time, we can replace the old_end makes the relatiobship reverse to new_start -> new_end
        # why dont we store it backward, new_start -> old_end, logically, it feels more natural because we just mirror what old_start do
        # however, when we look up, we check each new_start, it will lead to old_end, but we dont have the map from old_end and new_end, so the memo itself wont help us to build new_start to new_end relationship
        
        while start:
            new_node = Node(start.val)
            old_new_map[start] = new_node
            prev.next = new_node
            start = start.next
            prev = new_node
        
        prev.next =None
        # print(old_new_map)
        
        p1 = head
        p2 = dummy.next 
        while p1:
            # print(f"turn: {start.val}")
            if p1.random:
                p2.random = old_new_map[p1.random]
            p1 = p1.next
            p2 = p2.next

        return dummy.next 
        

            


        
        