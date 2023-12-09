

# 24 ms, faster than 96.63%, 14.1 MB, less than 71.20% 
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while True:
            res += head.val
            if not head.next: break
            head = head.next
            res *= 2
        return res