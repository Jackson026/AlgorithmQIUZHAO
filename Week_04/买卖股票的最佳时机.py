class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        minprice = prices[0]
        dp = [0] * len(prices)
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)
        return dp[-1]

class Solution:
    def maxProfit(self, prices) -> int:
        #动态规划
        #  """
        # （1）思路：动态规划
        #         买卖股票的实质就是：每个元素后面的最大值和当前元素的差，作为该元素为买点的最大利润，那么最佳时机就是这个
        #     差的最大值。
        #         以dp数组记录每个元素右边出现的最大值，即dp[i]代表第 i 元素的右边最大值。那么dp[i-1]和dp[i]存在如下关系：
        #     dp[i] = max(prices[i+1], dp[i+1])，从而最大利润则为max(dp[i]-prices[i])
        # （2）复杂度：
        #     - 时间复杂度：O（n）
        #     - 空间复杂度：O（n） 当然，不用dp数组储存直接用常量储存也行，复杂度变为O(1)
        # """

        n=len(prices)
        if n==0:
            return 0
        minprice=prices[0]
        dp=[0]*n
        for i in range(1,n):
            minprice=min(minprice,prices[i])
            dp[i]=max(dp[i-1],prices[i]-minprice)
        return dp[-1]
