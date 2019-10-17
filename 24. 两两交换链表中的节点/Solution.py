# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: 
            return head
        
        p_head = head
        res = ListNode(None)
        p_res = res
        p_head = head.next.next

        p_res.next = head.next
        p_res = p_res.next
        p_res.next = head
        p_res = p_res.next
        p_res.next = self.swapPairs(p_head)
        return res.next