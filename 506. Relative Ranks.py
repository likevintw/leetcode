

class Solution:
    '''
    201 ms, 23.50%, 16 MB, 6.35%
    '''

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

            @staticmethod
            def insert(root, val):
                if not root:
                    return TreeNode(val)
                if val <= root.val:
                    root.left = TreeNode.insert(root.left, val)
                else:
                    root.right = TreeNode.insert(root.right, val)
                return root

            @staticmethod
            def get_inorder_traversal_list(root):
                result = {}

                def inorder_traversal(root):
                    if root.left:
                        inorder_traversal(root.left)
                    rank = len(result)+1
                    result.update({root.val: rank})
                    if root.right:
                        inorder_traversal(root.right)
                inorder_traversal(root)
                return result

        root = None
        for i in range(len(score)):
            root = TreeNode.insert(root, score[i])
        buffer = TreeNode.get_inorder_traversal_list(root)

        result = []
        for i in score:
            rank = len(score)-buffer[i]+1
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))
        return result


class Solution:
    '''
    115 ms, 49.86%, 15.3 MB, 21.79%
    '''

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_list = sorted(score, reverse=True)
        table = {}
        for i in range(len(rank_list)):
            table.update({rank_list[i]: i+1})
        result = []
        for i in range(len(score)):
            rank = table[score[i]]
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))
        return result
