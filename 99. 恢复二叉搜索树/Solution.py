# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        def dfs(root: TreeNode) -> None:
            if root == None:
                return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
            return
        dfs(root)
        print(inorder)
        first, second = None, None
        flag = False
        for i in range(1, len(inorder)):
            if flag == False and inorder[i].val < inorder[i-1].val:
                first = inorder[i-1]
                flag = True
            if flag == True and inorder[i].val < inorder[i-1].val:
                second = inorder[i]
        first.val, second.val = second.val, first.val
        return