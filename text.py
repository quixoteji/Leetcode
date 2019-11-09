import collections
def moveZeroes(nums):
    if len(nums) < 2 : return nums
    p, q = 0, 0
    while q < len(nums) :
        if nums[q] == 0 : 
            q += 1
        else :
            nums[p], nums[q] = nums[q], nums[p]
            p += 1

moveZeroes([1,2])
