# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        res = ListNode(None)
        point = res
        dumb = ListNode(None)
        dumb.next = head
        head = dumb
        slow, fast = head, head.next
        while not fast == None:
            if fast.val < x:
                point.next = fast
                slow.next = fast.next
                point = point.next
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        point.next = head.next
        return res.next