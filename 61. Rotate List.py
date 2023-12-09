


# 32 ms, 92.16%, 14.4 MB, 32.95%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #
        if head == None: return head
        if head.next == None: return head
        
        # get list number
        node_number = 1
        current = head
        while (current):
            # print(current.val)
            current = current.next
            node_number += 1
            if current.next == None: 
                current.next = head
                break
        latest_node = current
        # print("node_number: ",node_number)
        # print("latest_node: ",latest_node.val)
        
        # get updated k
        k = node_number-k%(node_number)
        # print("k: ", k)
        
        # 
        current = head
        while (current):
            if k == 1: 
                latest_node = current
            if k == 0: 
                answer = current
                break
            current = current.next
            k-=1
        latest_node.next = None
        
        
        return answer
        