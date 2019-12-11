# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def iterator(node, remain):
            if node.left == None and node.right == None:
                return remain == node.val
            elif node.left != None and node.right != None:
                return iterator(node.left, remain-node.val) or iterator(node.right, remain-node.val)
            elif node.left == None and node.right != None:
                return iterator(node.right, remain-node.val)
            else:
                return iterator(node.left, remain-node.val)
        if root == None: return False
        return iterator(root, sum)