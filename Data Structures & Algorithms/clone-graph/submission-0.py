"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if not node:
                return
            new_node = Node(node.val)
            visited[node.val] = new_node

            for nxt in node.neighbors:
                if nxt.val not in visited:
                    nxt_node = dfs(nxt)
                else:
                    nxt_node = visited[nxt.val]
                new_node.neighbors.append(nxt_node)
            return new_node
        visited = {}

        return dfs(node)