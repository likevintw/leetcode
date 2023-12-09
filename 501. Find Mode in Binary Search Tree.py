

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# unfinished
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        sequence_lest = []
        hash_table = {}
        def search_LVR(root: TreeNode):
            if root.left: search_LVR(root.left)
            sequence_lest.append(root.val)
            if root.right: search_LVR(root.right)
                
        def most_common_number(input_list):
            threshold = 0
            buffer = 0
            res = []
            for i in input_list:
                if i in hash_table.values(): pass
                else:
                    buffer = input_list.count(i)
                    hash_table.update({buffer:i})
                    if buffer > threshold : 
                        threshold = buffer
            print(hash_table)
            for i in hash_table.keys():
                if i == threshold:
                    if hash_table[i] in res: pass
                    else: res.append(hash_table[i])
            return res
                    
        if root==None: return []
        search_LVR(root)
        # print(most_common_number)
        return most_common_number(sequence_lest)
    
# 1816 ms, faster than 5.17% , 18.2 MB, less than 73.51%
'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        sequence_lest = []
        def search_LVR(root: TreeNode):
            if root.left: search_LVR(root.left)
            sequence_lest.append(root.val)
            if root.right: search_LVR(root.right)
                
        def most_common_number(input_list):
            threshold = 0
            buffer = 0
            res = None
            for i in input_list:
                buffer = input_list.count(i)
                if buffer > threshold : 
                    threshold = buffer
                    res = [i]
                if buffer == threshold : 
                    if i in res: pass
                    else: res.append(i)
            
            return res
                    
        if root==None: return []
        search_LVR(root)
        # print(most_common_number)
        return most_common_number(sequence_lest)
'''