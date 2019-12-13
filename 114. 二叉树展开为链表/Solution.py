# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        queue = []
        stack = [root]
        while stack != []:
            cur = stack.pop()
            queue.append(cur)
            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
        for i in range(1, len(queue)):
            queue[i-1].right = queue[i]
            queue[i-1].left = None