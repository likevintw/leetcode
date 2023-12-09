
def quicksort(nums, left, right):
    if left >= right:
        return

    i = left
    j = right

    while i != j:
        while nums[j] > nums[left]:
            j -= 1
        while nums[i] <= nums[left] and i < j:
            i += 1
        print(nums)
        nums[i], nums[j] = nums[j], nums[i]
        
    print(nums)
    nums[left],  nums[i] = nums[i], nums[left]

    quicksort(nums, left, i-1)
    quicksort(nums, i+1, right)

    return nums


tests = []
tests.append([3, 2, 1, 5, 6, 4])
tests.append([89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23])
tests.append([4, 5, 3, 8, 6, 2, 1])

for nums in tests:
    tester = quicksort(nums, 0, len(nums)-1)
    answer = sorted(nums)
    print(tester)
    print(answer)
    assert tester == answer
    break
