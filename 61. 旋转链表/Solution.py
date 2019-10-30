# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count = 0
        p_node = head
        while p_node != None:
            count += 1
            p_node = p_node.next
        if count == 0: return None
        if k % count == 0: return head
        new_head_i = count - k % count
        new_head = None
        p_node = head
        for _ in range(new_head_i-1):
            p_node = p_node.next
        new_head = p_node.next
        p_node.next = None
        p_node = new_head
        while p_node.next != None:
            p_node = p_node.next
        p_node.next = head
        return new_head