# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == m: return head
        dumb = ListNode(None)
        dumb.next = head
        head = dumb
        index = 0
        p = head
        while index <= n:
            if index < m - 1:
                p = p.next
            elif index == m - 1:
                brk_head = p
                p = p.next
            elif index == m:
                temp2 = p
                brk_tail = p.next.next
                temp = p.next
                p.next.next = p
                p = brk_tail
                index += 1
            else:
                brk_tail = brk_tail.next
                p.next = temp
                temp = p
                p = brk_tail
            index += 1
        brk_head.next = temp
        temp2.next = brk_tail
        return head.next