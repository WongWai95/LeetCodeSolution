# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p_head = head
        
        for _ in range(k):
            if p_head == None:
                return head
            else:
                p_head = p_head.next
                
        res = ListNode(None)
        p_res = res
        
        candidate = [None for _ in range(k)]
        for i in range(k-1, -1, -1):
            candidate[i] = head
            head = head.next
        for i in range(k):
            p_res.next = candidate[i]
            p_res = p_res.next
            
        p_res.next = self.reverseKGroup(p_head, k)
        return res.next