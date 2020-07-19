# 通过交换位置来在原数组上完成任务

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums