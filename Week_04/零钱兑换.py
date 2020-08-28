import math


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # DP method
        # dp=[float('inf')]*(amount+1)
        # dp[0]=0
        # for c in coins:
        #     for i in range(c,amount+1):
        #         dp[i]=min(dp[i],dp[i-c]+1)
        # return dp[amount] if dp[amount]!=float('inf') else -1

        # dp=[0]+[float('inf')]*amount
        # for i in range(1,amount+1):
        #     for c in coins:
        #         if i>=c:
        #             dp[i]=min(dp[i],dp[i-c]+1)
        # return dp[amount] if dp[amount]!=float('inf') else -1

        # DFS method
        n = len(coins)
        coins.sort(reverse=True)     # 先给硬币排序，降序
        self.res = float("inf")      # 定义最小的使用硬币的数量为self.res

        def dfs(index,target,count):   # 定义深度优先搜索算法
            coin = coins[index]
            if math.ceil(target/coin)+count>=self.res:
                return
            if target%coin==0:
                self.res = count+target//coin
            if index==n-1:return
            for j in range(target//coin,-1,-1):
                dfs(index+1,target-j*coin,count+j)

        # dfs(0,amount,0)
        # return int(self.res) if self.res!=float("inf") else -1

        # 广度优先遍历BFS
        # if amount<0:return -1
        # stack=[[0,0]]
        # visited=set()
        # while stack:
        #     num,res=stack.pop(0)
        #     if num == amount:return res
        #     if num<amount:
        #         res+=1
        #         for c in coins:
        #             t=num+c
        #             if t in visited:
        #                 continue
        #             visited.add(t)
        #             stack.append([t,res])
        # return -1