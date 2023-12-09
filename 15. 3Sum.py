
class Solution:
    ''' pointers '''
    ''' 742 ms, 90.01% 18.1 MB, 74.16% '''
    ''' 
    time:   O(n^2)
    space:  O(1)
    '''

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result


# reference C++, 96%
"""
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
	vector<vector<int>> result;
	if (nums.empty()) {
		return result;
	}

	int n= nums.size();
	sort(nums.begin(), nums.end());
	for (int i = 0; i < n; i++) {
		if (nums[i] > 0) {
            break;
        }
		if (i > 0 and nums[i] == nums[i-1]){
            continue;
        }
		int left = i+1, right = n - 1;
		while (left < right) {
			int sum = nums[i] + nums[left] + nums[right];
			if (sum < 0) {
				left++;
			} else if (sum > 0) {
				right--;
			} else {
				result.push_back({nums[i], nums[left], nums[right]});
				int last_left = nums[left], last_right = nums[right];
				while (left < right && nums[left] == last_left) left++;
				while (left < right && nums[right] == last_right) right--;
			}
		}

	}
	return result;
}
};
"""
