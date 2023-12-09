# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    ''' DFS '''
    '''
    Time Complexity O(N)
    Space Complexity O(h) 
    '''
    ''' 38 ms,  67.02% 13.8 MB,  79.19%'''

    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution(object):
    ''' queue '''
    ''' 63 ms, 8.96% 13.9 MB, 79.19% '''

    def isSameTree(self, p, q):
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return n1 == n2
            if n1.val != n2.val:
                return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True


class Solution(object):
    ''' Stack '''
    ''' 25 ms, 96.59%  14 MB, 33.51% '''

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return n1 == n2
            if n1.val != n2.val:
                return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True
