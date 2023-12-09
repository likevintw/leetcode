# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#

#24 ms 97.06%, 14.4 MB, 8.49%
''''''
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res = []
        def get_tree_sequence(root: TreeNode):
            if root.left: get_tree_sequence(root.left)
            # res_list.append(root.val)
            if root.left == None and root.right == None: 
                res.append(root.val)
                # print(root.val)
            if root.right: get_tree_sequence(root.right)
        
        get_tree_sequence(root1)
        root1_res = res
        print(res)
        res = []
        get_tree_sequence(root2)
        root2_res = res
        print(res)
        if root1_res == root2_res: return True
        else: False

            