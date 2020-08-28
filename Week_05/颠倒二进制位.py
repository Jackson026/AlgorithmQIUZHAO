class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

'''

关键思想是，对于位于索引 i 处的位，在反转之后，其位置应为 31-i（注：索引从零开始）。

我们从右到左遍历输入整数的位字符串（即 n=n>>1）。要检索整数的最右边的位，我们应用与运算（n&1）。
对于每个位，我们将其反转到正确的位置（即（n&1）<<power）。然后添加到最终结果。
当 n==0 时，我们终止迭代。
PythonC++Go

'''
