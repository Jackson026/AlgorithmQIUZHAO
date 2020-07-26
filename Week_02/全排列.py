
# 回溯算法

def permute(self, nums):
    res = []

    def backtrack(nums, t):
        if not nums:
            res.append(t)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i + 1:], t + [nums[i]])

    backtrack(nums, [])
    return res