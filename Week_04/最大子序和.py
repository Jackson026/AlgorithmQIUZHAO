class Solution:
    def maxSubArray(self, nums) -> int:
        dp=nums
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])   # 比较当前值与前一个值加当前值的大小
            # dp[i]=max(dp[i-1],0)+nums[i]
        return max(dp)