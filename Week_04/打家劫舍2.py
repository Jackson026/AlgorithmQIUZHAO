class Solution:
    def rob(self, nums) -> int:
        if not nums:return 0
        if len(nums)==1:return nums[0]
        def abc(nums):
            if len(nums)==0:return 0
            if len(nums)==1:return nums[0]
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        return max(abc(nums[:-1]),abc(nums[1:]))




        # def d(nums):
        #     pre,cur=0,0
        #     for i in nums:
        #         pre,cur=cur,max(cur,pre+i)
        #     return cur
        # return max(d(nums[:-1]),d(nums[1:])) if len(nums)!=1 else nums[0]