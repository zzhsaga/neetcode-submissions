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
        randomMemo = {}
        dummy = Node(0)
        prev = dummy
        start = head

        while start:
            new_node = Node(start.val)
            if start.random:
                if start.random not in randomMemo:
                    randomMemo[start.random] = [new_node]
                else:
                    randomMemo[start.random].append(new_node)
            prev.next = new_node
            start = start.next
            prev = new_node
        
        prev.next =None
        print(randomMemo)
        
        start = head
        start_new = dummy.next 
        while start:
            # print(f"turn: {start.val}")
            if start in randomMemo:
                for node in randomMemo[start]:
                    # print(node.val, start_new.val)
                    node.random = start_new
            start = start.next
            start_new = start_new.next
        
        # map as all new_nodes
        # 5 -> 7, 7 appear before 5, 
        # create new_7
        # 7 -> store (5,new_7)
        # we make sure every step, we have the new node

        # second time go throught the LL
        # we do a syncize iteration




        return dummy.next 
        

            


        
        