

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # reference
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:return False
        
        #check if leaf node and target sum achieved
        if sum==root.val and root.left==None and root.right==None: return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# reference
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        #check if leaf node and target sum achieved
        if sum==root.val and root.left==None and root.right==None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
'''