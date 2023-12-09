

# 120 ms, faster than 53.42% 14.1 MB, less than 98.63%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table_dict = {}
        buffer = 0
        for i in range(len(nums)):
            if nums[i] in table_dict.keys(): 
                buffer = table_dict[nums[i]]
                table_dict.update({nums[i]:buffer+1})
            else :
                table_dict.update({nums[i]:1})
        # print(table_list)
        # print(table_dict)
        res = []
        buffer = 0
        for i in nums:
            buffer = 0
            for j in table_dict.keys():
                if i>j: buffer += table_dict[j]
            res.append(buffer)
        return res
        
# 124 ms, faster than 53.10% Memory Usage: 14.3 MB, less than 75.63% 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table_dict = {}
        table_list = []
        buffer = 0
        for i in range(len(nums)):
            if nums[i] in table_list: 
                buffer = table_dict[nums[i]]
                table_dict.update({nums[i]:buffer+1})
            else :
                table_dict.update({nums[i]:1})
                table_list.append(nums[i])
        # print(table_list)
        # print(table_dict)
        res = []
        buffer = 0
        for i in nums:
            buffer = 0
            for j in table_dict.keys():
                if i>j: buffer += table_dict[j]
            res.append(buffer)
        return res
            
            
        

# 544 ms, faster than 8.22% 14.4 MB, less than 48.90%
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = []
#         check = 0
#         for i in range(len(nums)):
#             check = 0
#             for j in range(len(nums)):
#                 if i == j: continue
#                 if nums[i] > nums[j]: check += 1
#             res.append(check)
#         return res
                

# 120 ms, faster than 53.16% 14.4 MB, less than 48.90%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table_dict = {}
        table_list = []
        
        for i in range(len(nums)):
            if nums[i] in table_list: 
                buffer = table_dict[nums[i]][0]
                table_dict.update({nums[i]:[buffer+1]})
            else :
                table_dict.update({nums[i]:[1]})
                table_list.append(nums[i])
        # print(table_list)
        # print(table_dict)
        res = []
        buffer = 0
        for i in nums:
            buffer = 0
            for j in table_dict.keys():
                if i>j: buffer += table_dict[j][0]
            res.append(buffer)
        return res
            
            
        

# 544 ms, faster than 8.22% 14.4 MB, less than 48.90%
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = []
#         check = 0
#         for i in range(len(nums)):
#             check = 0
#             for j in range(len(nums)):
#                 if i == j: continue
#                 if nums[i] > nums[j]: check += 1
#             res.append(check)
#         return res
                