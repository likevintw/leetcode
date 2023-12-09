

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.sum_table = [0]
        for i in range(len(nums)):
            self.sum_table.append(self.sum_table[i]+nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i==0: return self.sum_table[j+1]
        else: return self.sum_table[j+1]-self.sum_table[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)