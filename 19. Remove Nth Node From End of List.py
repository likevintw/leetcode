# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ''' two pointers, wanderful '''
    ''' 40 ms, 68.68% 13.8 MB, 73.45% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        p = result
        s = f = head
        i = 0
        while f:
            if i >= n:
                p = s
                s = s.next
                f = f.next
            else:
                f = f.next
            i += 1
        p.next = s.next
        return result.next
