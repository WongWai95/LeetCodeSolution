# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 统计链表a和b的长度
        a_count, b_count = 0, 0
        node = headA
        while node != None:
            a_count += 1
            node = node.next
        node = headB
        while node != None:
            b_count += 1
            node = node.next
        
        a_node = headA
        b_node = headB
        if a_count > b_count:
            skip = a_count - b_count
            for _ in range(skip):
                a_node = a_node.next
        else:
            skip = b_count - a_count
            for _ in range(skip):
                b_node = b_node.next
        while a_node != None:
            if a_node == b_node:
                return a_node
            a_node = a_node.next
            b_node = b_node.next
        return None