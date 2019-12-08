# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        pool = []
        while head != None:
            pool.append(head.val)
            head = head.next
        def iterator(nums):
            if nums == []: return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = iterator(nums[:mid])
            node.right = iterator(nums[mid+1:])
            return node
        return iterator(pool)