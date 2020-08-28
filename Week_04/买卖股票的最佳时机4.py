class Solution:
    def maxProfit(self, k: int, prices) -> int:
        # 定义卖出股票,交易次数 j + 1
        # dp[i][j][0] 今天是第i天 进行 j次 交易 手上没有股票
        # dp[i][j][1] 今天是第i天 进行 j次 交易 手上有股票
        if k == 0 or len(prices) < 2:
            return 0
        n = len(prices)
        res = []
        if k > n // 2:
            max_profit = 0
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]
                if profit > 0:
                    max_profit += profit
            return max_profit

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(k + 1):
                if not j:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])  # 在j-1天卖出
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])  # 在第j天买

        for m in range(k + 1):
            res.append(dp[-1][m][0])
        return max(res)
