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
        if root == None: return None
        to_open = [root]
        temp = []
        while to_open != []:
            while to_open != []:
                cur = to_open.pop(0)
                if cur.left != None:
                    temp.append(cur.left)
                if cur.right != None:
                    temp.append(cur.right)
            for i in range(len(temp)-1):
                temp[i].next = temp[i+1]
            if temp != []:    
                temp[-1].next = None
            to_open = temp[:]
            temp = []
        return root