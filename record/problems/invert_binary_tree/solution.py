# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return node 
            leftnode = invert(node.left)
            rightnode = invert(node.right)
            # swap
            node.left, node.right = rightnode, leftnode 
            return node 
        return invert(root)