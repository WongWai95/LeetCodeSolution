# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def iterator(node: TreeNode, depth: int) -> int:
            if node != None:
                return max(iterator(node.right, depth+1), iterator(node.left, depth+1))
            else:
                return depth - 1
        return iterator(root, 1)