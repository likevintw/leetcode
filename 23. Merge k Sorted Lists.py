

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    96 ms, 96.96% ,18.4 MB, 20.54%
    time: 2n + nlogn(sort)
    space: n + n (sort)
    '''

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for i in lists:
            pointer = i
            while pointer:
                numbers.append(pointer.val)
                pointer = pointer.next
        numbers.sort()
        result = ListNode(0, None)
        cur = result
        for i in numbers:
            cur.next = ListNode(i, None)
            cur = cur.next
        return result.next
