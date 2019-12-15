"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = [root]
        id = 0
        crit = 2
        while not queue == []:
            cur = queue.pop(0)
            id += 1
            if cur.left != None and cur.right != None:
                queue.append(cur.left)
                queue.append(cur.right)
            if id == crit - 1:
                cur.next = None
                crit *= 2
            else:
                cur.next = queue[0]
        return root