

# 40 ms, 87.30%, 13.9 MB, 79.37% 
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def _slop(a,b):
            if a == 0: return [0, a/b]
            return [1, b/a]
        
        a = coordinates[1][0]-coordinates[0][0]
        b = coordinates[1][1]-coordinates[0][1]
        res = _slop(a,b)
         
        for i in range(1, len(coordinates)-1):
            a = coordinates[i+1][0]-coordinates[i][0]
            b = coordinates[i+1][1]-coordinates[i][1]
            if res != _slop(a,b): return False 
            
        return True

if __name__ == "__main__":
    tester = SolutionA()