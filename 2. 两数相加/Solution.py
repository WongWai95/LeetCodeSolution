# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        loop_flag = True
        ret_head = ListNode(None)
        ret_pointer = ret_head
        
        while loop_flag:
            if l1==None and l2==None:
                loop_flag = False
                if overflow==1:
                    ret_pointer.next = ListNode(1)
                    ret_pointer = ret_pointer.next
                    ret_pointer.next = None
                else:
                    ret_pointer.next = None
            elif l1==None:
                ret_val = l2.val + overflow
                if ret_val>=10:
                    ret_val -= 10
                    overflow = 1
                else:
                    overflow = 0
                l2 = l2.next
                ret_pointer.next = ListNode(ret_val)
                ret_pointer = ret_pointer.next
            elif l2==None:
                ret_val = l1.val + overflow
                if ret_val>=10:
                    ret_val -= 10
                    overflow = 1
                else:
                    overflow = 0
                l1 = l1.next
                ret_pointer.next = ListNode(ret_val)
                ret_pointer = ret_pointer.next
            else:
                ret_val = l1.val + l2.val + overflow
                if ret_val>=10:
                    ret_val -= 10
                    overflow = 1
                else:
                    overflow = 0
                l1 = l1.next
                l2 = l2.next
                ret_pointer.next = ListNode(ret_val)
                ret_pointer = ret_pointer.next
                
        return ret_head.next