# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' 1. '''

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_tree_level(node):
            if not node:
                return 0
            l = get_tree_level(node.left)
            r = get_tree_level(node.right)
            return l+1 if l > r else r+1

        if not root:
            return True
        l = get_tree_level(root.left)
        r = get_tree_level(root.right)
        if abs(r-l) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
