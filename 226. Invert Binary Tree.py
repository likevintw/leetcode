# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' own idea '''
    ''' 54 ms, 22.19% 13.8 MB, 96.54% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        return root


class Solution:
    ''' better implement '''
    ''' 29 ms, 91.21% 14 MB,  12.18% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root
