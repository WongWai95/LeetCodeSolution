"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hash_dict = {}
        if head == None: return None

        # copy the NEXT
        prev = head
        new_prev = new_cur = Node(prev.val)
        hash_dict[id(prev)] = new_prev
        cur = head.next
        while cur != None:
            new_cur = Node(cur.val)
            hash_dict[id(cur)] = new_cur
            new_prev.next = new_cur
            new_prev = new_cur
            prev = cur
            cur = cur.next
        hash_dict[id(cur)] = None
        new_cur.next = None

        # copy the RANDOM
        cur = head
        while cur != None:
            hash_dict[id(cur)].random = hash_dict[id(cur.random)]
            cur = cur.next

        return hash_dict[id(head)]