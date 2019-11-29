# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []: return None
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i
        cur_node_val = preorder[0]
        cur_node = TreeNode(cur_node_val)
        cur_node.left = self.buildTree(preorder[1:hash_map[cur_node_val]+1], inorder[0:hash_map[cur_node_val]])
        cur_node.right = self.buildTree(preorder[hash_map[cur_node_val]+1:], inorder[hash_map[cur_node_val]+1:])
        return cur_node