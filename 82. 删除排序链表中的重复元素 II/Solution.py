# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dumb_node = ListNode(None)
        dumb_node.next = head
        head = dumb_node
        p = head.next
        mem = []
        while p != None:
            mem.append(p)
            p = p.next
        same_flag = False
        mem.append(ListNode(None))
        for i in range(len(mem)-1):
            if mem[i].val != mem[i+1].val:
                if same_flag == False:
                    continue
                else:
                    same_flag = False
                    mem[i] = None
            else:
                same_flag = True
                mem[i] = None
        p = head
        for i in range(len(mem)-1):
            if mem[i] != None:
                p.next = mem[i]
                p = mem[i]
        p.next = None
        return head.next