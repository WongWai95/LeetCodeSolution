# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def split(head: ListNode) -> [ListNode, ListNode]:
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            if slow == fast:
                return [None, slow]
            mid = head
            while mid.next != slow:
                mid = mid.next
            mid.next = None
            return [head, slow]

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            head = cur = ListNode(None)
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            if not head2:
                cur.next = head1
            if not head1:
                cur.next = head2
            return head.next

        # print('-------\n', head)
        head1, head2 = split(head)
        # print('split', head1, head2)
        if not head1 or not head2:
            return merge(head1, head2)
        sorted1 = self.sortList(head1)
        # print('1 out')
        sorted2 = self.sortList(head2)
        # print('2 out')
        sorted = merge(sorted1, sorted2)
        # print('merge:', sorted)
        return sorted