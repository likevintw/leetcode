class Solution:
    ''' buffer flag '''
    ''' 37 ms, 80.70% 13.9 MB, 90.84% '''
    '''
        time: O(m*n), n is the length of answer 
        space: O(n), a string buffer
    '''

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        result = strs[0]
        for i in range(1, len(strs)):
            buffer = min(len(strs[i]), len(result))
            for j in range(buffer):
                if result[j] == strs[i][j]:
                    continue
                else:
                    result = result[:j]
                    break
            if len(result) > len(strs[i]):
                result = strs[i]
        return result


class Solution:
    ''' flag '''
    ''' 32 ms, 95.40% 14 MB, 13.52% '''
    '''
        time: O(m*n)
        space: O(1), a int variable
    '''

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [] or "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        diff = len(strs[0])
        for i in strs:
            diff = len(i) if len(i) < diff else diff
            for j in range(diff):
                if i[j] != strs[0][j]:
                    diff = j
                    break
        return strs[0][:diff]
