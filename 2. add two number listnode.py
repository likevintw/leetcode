
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#(88 ms,10.35%,13.4 MB,29.73%)
#(72 ms,21.99%,13.4 MB,29.73%)
class SolutionA(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        l1.val
        l1.
        """
        list_1 = []
        list_2 = []
        while True:
            if l1 != None: list_1.append(l1.val)
            if l1.next != None: l1 = l1.next
            else: break
        while True:
            if l2 != None: list_2.append(l2.val)
            if l2.next != None: l2 = l2.next
            else: break
        print(list_1)
        print(list_2)
        list_res = []
        size = len(list_1)
        if len(list_2) > len(list_1): size = len(list_2)
        
        promote = 0
        for i in range(size):
            a = 0
            b = 0
            if i < len(list_1): a = list_1[i]
            if i < len(list_2): b = list_2[i]
            temp_sum = promote+a+b
            if temp_sum > 9: 
                list_res.append(temp_sum-10)
                promote = 1
            else: 
                list_res.append(temp_sum)
                promote = 0
            if i == size-1 and promote == 1: list_res.append(promote)
        print(list_res)
        
        head = None
        res = None
        for i in range(len(list_res)):
            temp = ListNode(val=list_res[i])
            if head == None: 
                res = temp
                head = temp
            else: 
                res.next = temp
                res = res.next
    
                
        return head


    