
#回溯算法

def permuteUnique(self, nums):
    res = []

    def helper(nums, t):
        if not nums:
            res.append(t)
            return
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            helper(nums[:i] + nums[i + 1:], t + [nums[i]])
            visited.add(nums[i])

    helper(nums, [])
    return res