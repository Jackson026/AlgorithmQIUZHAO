class Solution:
    def lengthOfLIS(self, nums) -> int:
        # if not nums:return 0
        # dp=[1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)

        if not nums:
            return 0
        if len(nums)<2:
            return 1
        dp=[nums[0]]
        for n in range(1,len(nums)):
            if nums[n]>dp[-1]:
                dp.append(nums[n])
            else:
                l,r=0,len(dp)-1
                while l<=r:
                    mid=(l+r)//2
                    if nums[n]>dp[mid]:
                        l=mid+1
                    else:
                        r=mid-1
                dp[l]=nums[n]
        return len(dp)