

# 696 ms, 27.44%, 24.1MB, 5.12%
class SolutionA(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        import heapq
        diff = []
        _buffer = 0
        for i in range(len(heights)):
            if i < (len(heights)-1):
                _buffer = heights[i+1]-heights[i]
                _buffer = _buffer if _buffer > 0 else 0
                if _buffer > 0: 
                    heapq.heappush(diff,_buffer)
                    if len(diff) > ladders: 
                        bricks = bricks - heapq.heappop(diff)
                    if bricks < 0: return i
                else: pass
            #print(i,_buffer,diff,bricks)
        return len(heights)-1


if __name__ == "__main__":
    tester = SolutionA()
    