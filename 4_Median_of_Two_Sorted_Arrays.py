

# 92 ms, 68.93%, 14.6 MB, 24.30%       
# 88 ms, 84.40%, 14.5 MB, 55.69%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float::
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length%2 == 0: 
            length = int(length/2)
            return float((nums[length-1]+nums[length])/2)
        else:
            return nums[(int((length-1)/2))]

if __name__ == "__main__":
    pass

