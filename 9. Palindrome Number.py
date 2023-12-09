


class Solution:
    ''' 66 ms, 82.20% 13.8 MB, 63.92% '''
    ''' 
        time: O(n/2)
        space: O(1)
    '''

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        flag = len(x)-1
        for i in range(len(x)):
            if not x[i] == x[flag]:
                return False
            flag -= 1
        return True
