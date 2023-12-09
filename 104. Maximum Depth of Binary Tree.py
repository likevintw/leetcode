

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ''' recursion, if loop '''
    ''' 37 ms, 95.49% 16.3 59.04%  '''

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return l+1 if r < l else r+1


class Solution:
    ''' recursion, max '''
    ''' 44 ms, 85.61% 16.2 MB, 59.04% '''

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
