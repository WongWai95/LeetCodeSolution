# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        hash_set = set()
        node = head
        while node.next != None:
            if node in hash_set:
                return node
            hash_set.add(node)
            node = node.next
        return None