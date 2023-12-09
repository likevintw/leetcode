# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    ''' recursion '''
    ''' 39 ms, 86.60% 13.9 MB,  35.80% '''
    ''' 
    time:   O(n+m)
    space:  O(n+m) memory for recursive functions 
    '''

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class Solution:
    ''' iteration '''
    ''' 46 ms, 67.10% 13.8 MB, 82.94% '''
    ''' 
    time:   O(n+m)
    space:  O(1). the dummy node
    '''

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        c = result
        while list1 and list2:
            if list1.val < list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        if list1:
            c.next = list1
        if list2:
            c.next = list2
        return result.next
