# Definition for singly-linked list.
# class ListNode(0):
#     def __init__(p=resultself, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ''' iteration '''
    ''' 82 ms, 67.54% 17.8 MB, 83.01% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0)
        c = head
        p = result
        result.next = c

        while c:
            if c.val == val:
                p.next = c.next
                c = c.next
                continue
            p = p.next
            c = c.next
        return result.next
