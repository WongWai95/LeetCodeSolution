# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return None
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        res = [root.val]
        if right:
            res = right + res
        if left:
            res = left + res
        return res