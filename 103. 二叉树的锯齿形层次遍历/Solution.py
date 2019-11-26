# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        stack = []
        res = []
        layer = []
        order = True
        while queue != [] or stack != []:
            if order:
                while queue != []:
                    cur_node = queue.pop(0)
                    if cur_node.left != None:
                        stack.append(cur_node.left)
                    if cur_node.right != None:
                        stack.append(cur_node.right)
                    layer.append(cur_node.val)
            if not order:
                for e in stack:
                    if e.left != None:
                        queue.append(e.left)
                    if e.right != None:
                        queue.append(e.right)
                while stack != []:
                    cur_node = stack.pop()
                    layer.append(cur_node.val)
            res.append(layer)
            layer = []
            order = not order
        return res