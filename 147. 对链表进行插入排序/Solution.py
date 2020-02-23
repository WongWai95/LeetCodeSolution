# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        numb = ListNode(-float('inf'))
        numb.next = head
        head = numb
        fast = head.next
        last = head
        while fast != None:
            cur = fast
            fast = fast.next
            if cur.val >= last.val:
                last = cur
                continue
            last.next = fast
            slow = head
            while slow != last:
                if cur.val <= slow.next.val:
                    cur.next = slow.next
                    slow.next = cur
                    break
                slow = slow.next
        return head.next