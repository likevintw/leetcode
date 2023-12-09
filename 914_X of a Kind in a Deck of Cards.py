
# reference
# great common divisor (GCD)
# 132  ms, 36.84%, 13.9 MB, 59.87%
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter 
        element_num = []
        counter_res = Counter(deck)
        #print(counter_res)
        print(counter_res.values())
        _max = max(counter_res.values()) +1
        for i in range(2,_max):
            if all(j % i == 0 for j in counter_res.values()): return True
        return False


if __name__ == "__main__":
    tester = SolutionA()