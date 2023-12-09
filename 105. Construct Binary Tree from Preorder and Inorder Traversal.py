# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' 52 ms, 99.25% 18.9 MB, 74.63% '''

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional:
        # preorder=[3,9,20]
        # inorder=[9,3,20]
        counter = 0

        def turn_array_to_tree(left, right):
            nonlocal counter
            if left > right:
                return None
            value = preorder[counter]
            counter += 1
            index = per_to_in[value]
            node = TreeNode(value)
            node.left = turn_array_to_tree(left, index-1)
            node.right = turn_array_to_tree(index+1, right)
            return node

        per_to_in = {}
        for index, value in enumerate(inorder):
            per_to_in[value] = index
        return turn_array_to_tree(0, len(preorder) - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    ''' offical answer '''
    ''' 
    Time complexity : O(N).
    Space complexity : O(N).
    '''
    ''' 65 ms, 91.30% 18.9 MB, 74.63% '''

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional:
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(
                inorder_index_map[root_value] + 1, right)
            return root

        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


class Solution:
    ''' reference '''
    ''' 82 ms, 81.83% 18.8 MB, 90.40% '''
    ''' generator '''

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional:
        inorderLookup = {n: i for i, n in enumerate(inorder)}

        vals = iter(preorder)

        def dfs(left, right):
            if left > right:
                return None

            val = next(vals)
            node = TreeNode(val)

            split = inorderLookup[val]
            node.left = dfs(left, split - 1)
            node.right = dfs(split + 1, right)
            return node
        return dfs(0, len(preorder) - 1)


class Solution:
    ''' reference '''
    ''' 223 ms, 43.67% 53.4 MB, 56.00% '''

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
