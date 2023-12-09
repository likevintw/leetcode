# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ''' iteration '''
    ''' 34 ms, 79.65% 13.8 MB, 67.69%  '''
    '''
    time:   O(n)
    space:  O(1), dummy
    '''

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        i = 0
        result = ListNode(0)
        pp, p, c = result, head, head.next
        while c:
            if i % 2 == 0:
                pp.next = c
                p.next = c.next
                c.next = p
            pp = pp.next
            p = pp.next
            c = p.next
            i += 1

        return result.next
