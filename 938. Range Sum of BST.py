

# Best
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# wrose
# 244 ms, 43.63%, 22.3 MB, 17.00%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def get_range_sum(self, root):
        result = 0
        while True:
            if root.left:
                # result += checker(self.get_range_sum(root.left,checker))
                result += self.get_range_sum(root.left)
            if root.val <= self.max_num and root.val >= self.min_num:
                result += root.val
            if root.right:
                result += self.get_range_sum(root.right)
            return result

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.max_num = high
        self.min_num = low
        ans = self.get_range_sum(root)
        return ans
