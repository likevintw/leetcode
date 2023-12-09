# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ''' 57 ms, 85.02% 17.5 MB, 69.02% '''
    ''' fast point and slow point '''

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


class Solution:
    ''' 1474 ms, 5.02% 17.6 MB, 69.02% '''
    ''' table '''

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        table = []
        c = head
        while c:
            if c in table:
                return True
            table.append(c)
            c = c.next
        return False
