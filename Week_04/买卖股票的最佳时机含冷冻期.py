class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp=[[-prices[0],0,0]]+[[0]*3 for i in range(n-1)]
        # dp[i][0]:当天持有股票
        # dp[i][1]:当天不持有股票，且处于冷冻期
        # dp[i][2]:当天不持有股票，且不处于冷冻期
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1]=dp[i-1][0]+prices[i]
            dp[i][2]=max(dp[i-1][1],dp[i-1][2])
        return max(dp[-1][0],dp[-1][1],dp[-1][2])

        # if not prices:
        #     return 0
        # n=len(prices)
        # dp=[[-prices[0],0,0]]+[[0,0,0] for i in range(n-1)]
        # for i in range(1,n):
        #     dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i])
        #     dp[i][1]=dp[i-1][0]+prices[i]
        #     dp[i][2]=max(dp[i-1][1],dp[i-1][2])
        # return max(dp[n-1][1],dp[n-1][2])