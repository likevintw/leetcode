
# 4 ms, 100.00%, 13.3 MB, 88.42% 
# 20 ms, 35.47%, 13.4 MB, 63.55% 
# 32 ms, 5.67%, 13.5 MB, 35.22%
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def movement(k):
            k = int(k/2)
            if k < 1: return 1
            return k

        move = movement(n)
        position = move
        while(True):
            move = movement(move)
            if guess(position) == 1: position = position + move 
            elif guess(position) == -1: position = position - move
            elif guess(position) == 0: return position

if __name__ == "__main__":
    tester = SolutionA()