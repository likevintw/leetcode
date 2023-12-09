# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' DFS '''
    ''' 38 ms, 78.92% 14.3 MB, 53.75% '''
    '''
    time:   O(n)
    space:  O(n)
    '''

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, result = [root], [[root.val]]
        while len(queue) > 0:
            buffer = []
            for i in range(len(queue)):
                c = queue.pop(0)
                if c.left:
                    buffer.append(c.left.val)
                    queue.append(c.left)
                if c.right:
                    buffer.append(c.right.val)
                    queue.append(c.right)
            if len(buffer) > 0:
                result.append(buffer)
        return result
