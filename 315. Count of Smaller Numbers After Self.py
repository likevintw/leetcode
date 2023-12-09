

# kevin
# 164 ms, faster than 52.37% 19.7 MB, less than 11.02% 
class TreeNode:
    def __init__(self, _val):
        self.val = _val
        self.count = 1
        self.left = None
        self.right = None

def insert(current, value):
    smaller_count = 0
    node = TreeNode(value)
    while True:
        if node.val > current.val:
            smaller_count += current.count
            if current.right == None:
                current.right = node
                break
            else: current = current.right
        else:
            current.count += 1
            if current.left == None:
                current.left = node
                break
            else: current = current.left
    return smaller_count
    
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        res = [0]
        n = len(nums)
        head = TreeNode(nums[n-1])
        for i in range(len(nums)-2, -1, -1):
            res.append(insert(head, nums[i]))
        res.reverse()
        return res
        

# refernece
# 152 ms, faster than 63.83% 19.6 MB, less than 15.00%
class Node:
    def __init__(self, val):
        self.data = val
        self.count = 1
        self.left = None
        self.right = None

def insert(curr, val):
    node = Node(val)
    smaller = 0
    while True:
        if node.data <= curr.data:
            curr.count += 1
            if curr.left is None:
                curr.left = node
                break
            else:
                curr = curr.left
        else:
            smaller += curr.count
            if curr.right is None:
                curr.right = node
                break
            else:
                curr = curr.right
    return smaller

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # nums = [3,1,4,5,2,6,1,1]
        if nums is None or len(nums) == 0:
            return []
        res = [0]
        n = len(nums)
        root = Node(nums[n - 1])
        for i in range(n - 2, -1, -1):
            res.append(insert(root, nums[i]))
        res.reverse()
        return res