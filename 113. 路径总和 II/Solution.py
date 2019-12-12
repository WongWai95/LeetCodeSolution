# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def iterator(node, remain, path):
            if node.left == None and node.right == None:
                if remain == node.val:
                    path.append(remain)
                    res.append(path)
            elif node.left != None and node.right != None:
                iterator(node.left, remain-node.val, path+[node.val])
                iterator(node.right, remain-node.val, path+[node.val])
            elif node.left != None and node.right == None:
                iterator(node.left, remain-node.val, path+[node.val])
            else:
                iterator(node.right, remain-node.val, path+[node.val])
            return
        if root == None: return []
        iterator(root, sum, [])
        return res