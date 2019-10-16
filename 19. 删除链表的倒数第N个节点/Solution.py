# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p_n = head
        p_node = head
        index = 0
        
        while not p_node.next == None:
            if index >= n:
                p_n = p_n.next
            p_node = p_node.next
            index += 1
        if index < n:
            return head.next
        else:
            p_n.next = p_n.next.next
        return head