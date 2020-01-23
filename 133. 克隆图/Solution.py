"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        connection = {}
        stack = [node]
        new = Node(node.val)
        connection[id(node)] = new
        while not stack == []:
            cur = stack.pop()
            for nb in cur.neighbors:
                if id(nb) not in connection:
                    new = Node(nb.val)
                    connection[id(nb)] = new
                    stack.append(nb)
                connection[id(cur)].neighbors.append(connection[id(nb)])
        return connection[id(node)]