def threeSum(nums):
    n = len(nums)
    nums.sort()
    if not nums or n < 3:
        return []
    res = []
    for i in range(n):
        if nums[i] > 0:
            return res
        l, r = i + 1, n - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            elif nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res

#思路就是把式子变成a+b=-c,然后利用排序+双指针套路来进行运算
#拍序数组是前提，然后注意是不重复的三个数，所以有重复项要跳过