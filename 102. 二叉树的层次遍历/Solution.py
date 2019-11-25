# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root, None]
        res = []
        layer = []
        while queue != []:
            cur_node = queue[0]
            queue.pop(0)
            if cur_node == None:
                res.append(layer)
                layer = []
                queue.append(None)
                if queue[0] == None:
                    break
                else:
                    continue
            layer.append(cur_node.val)
            if cur_node.left != None:
                queue.append(cur_node.left)
            if cur_node.right != None:
                queue.append(cur_node.right)
        return res
