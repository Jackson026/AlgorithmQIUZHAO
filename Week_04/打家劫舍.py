class Solution:
    def rob(self, nums) -> int:
        cur,pre=0,0
        for i in nums:
            pre,cur=cur,max(cur,pre+i)
        return cur


        #dp[n]=max(dp[n-1],dp[n-2]+i)