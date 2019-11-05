# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dump = ListNode(None)
        dump.next = head
        slow = dump
        fast = head
        while fast != None:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return head