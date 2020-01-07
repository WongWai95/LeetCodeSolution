# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = []
        def iterator(node: TreeNode, path: list) -> None:
            path = path + [node.val]
            if node.left == None and node.right == None:
                num = ''
                for p in path:
                    num += str(p)
                num = int(num)
                nums.append(num)
                return
            if node.left != None:
                iterator(node.left, path)
            if node.right != None:
                iterator(node.right, path)
            return 
        if root == None: return 0
        iterator(root, [])
        sum = 0
        for e in nums:
            sum += e
        return sum