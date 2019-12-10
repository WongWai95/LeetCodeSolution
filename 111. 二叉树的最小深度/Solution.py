# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def iterator(root):
            if root.left == None and root.right == None:
                return 1
            elif root.left != None and root.right != None:
                return min(iterator(root.left), iterator(root.right)) + 1
            else:
                if root.left == None:
                    return iterator(root.right) + 1
                else:
                    return iterator(root.left) + 1
        if root == None:
            return 0
        return iterator(root)