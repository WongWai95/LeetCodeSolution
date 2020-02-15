# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        mem = []
        node = head
        while node:
            mem.append(node)
            node = node.next
        sign = 1
        index = 0
        last_i = 0
        for i in range(1, len(mem)):
            index += (len(mem) - i) * sign
            sign *= -1
            mem[last_i].next = mem[index]
            last_i = index
        mem[index].next = None
        return