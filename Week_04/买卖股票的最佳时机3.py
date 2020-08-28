class Solution:
    def maxProfit(self, prices) -> int:
        # 最多两次交易，可以拆成：
        # 只有一次交易（比较简单，直接从左到右遍历一遍记录最小值，然后记录当前价格减去最小值的收益）
        # 有两次交易 （需要选择两次交易的分割点，然后对左右两边的子数组分别计算一次交易的最大收益）

        # 两次交易计算：
        # 从左到右遍历一遍，记录每个位置的左边子数组的单词交易最大收益（同单次交易，直接复用）
        # 同理，从右到左遍历一遍，记录每个位置的右边子数组的单词交易最大收益
        # 然后再遍历一遍，找到两次交易的最佳分割点，即可得到两次交易情况下的最大收益
        # 选择两次交易最大收益和单词交易最大收益的较大值

        n=len(prices)
        if n<2:
            return 0
        l,r=[0]*n,[0]*n
        min_v=prices[0]
        for i in range(1,n):
            min_v=min(min_v,prices[i])
            l[i]=max(l[i-1],prices[i]-min_v)
        max_v=0
        for j in range(n-1,-1,-1):
            max_v=max(max_v,prices[j])
            r[j]=max(r[j],max_v-prices[j])
        two_v=0
        for k in range(1,n-1):
            two_v=max(two_v,l[k]+r[k])
        return max(two_v,l[-1])