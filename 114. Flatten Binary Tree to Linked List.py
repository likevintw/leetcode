# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' reference '''
    ''' 25 ms, 99.67% 15.3 MB, 48.85% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def __init__(self):
        self.pre = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.pre
        self.pre = root
