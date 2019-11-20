# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def iterator(root: TreeNode) -> (bool, int, int):
            if root == None:
                return True, 4294967296, -4294967295
            it_right = iterator(root.right)
            if it_right[0] == False:
                return False, -1, -1
            else:
                if it_right[1] <= root.val:
                    return False, -1, -1
            it_left = iterator(root.left)
            if it_left[0] == False:
                return False, -1, -1
            else:
                if it_left[2] >= root.val:
                    return False, -1, -1
            return True, min(root.val, it_right[1], it_left[1]), max(root.val, it_right[2], it_left[2])
        return iterator(root)[0]