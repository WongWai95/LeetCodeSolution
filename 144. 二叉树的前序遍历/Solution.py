# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return None
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res = [root.val]
        if left:
            res = res + left
        if right:
            res = res + right
        return res