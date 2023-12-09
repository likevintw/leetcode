

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 47 ms, 62.09%, 16.2 MB, 22.10%
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        pointer = head
        while pointer:
            new = ListNode(pointer.val, cur)
            cur = new
            pointer = pointer.next
        return cur
