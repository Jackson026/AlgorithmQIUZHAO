class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        # cash是不持有股票时的最大利润，hold表示当我们持有股票时的最大利润。
        # cash,hold=0,-prices[0]
        # n=len(prices)
        # for i in range(1,n):
        #     cash=max(cash,hold+prices[i]-fee)
        #     hold=max(hold,cash-prices[i])
        # return max(cash,hold)

        n=len(prices)
        if n<2:
            return 0
        dp=[[-prices[0],0]] + [[0,0] for i in range(n-1)]        # hold, unhold
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][0]+prices[i]-fee,dp[i-1][1])
        return max(dp[i][0],dp[i][1])