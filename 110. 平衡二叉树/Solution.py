# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def iterator(root):
            if root == None: return 0, 0, True
            left_node = iterator(root.left)
            right_node = iterator(root.right)
            return max(left_node[0]+1, left_node[1]+1), max(right_node[0]+1, right_node[1]+1), left_node[2] and right_node[2] and abs(max(left_node[0]+1, left_node[1]+1) - max(right_node[0]+1, right_node[1]+1)) <= 1
        res = iterator(root)
        print(res[0], res[1], res[2])
        return res[2]