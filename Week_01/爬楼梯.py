# 动态规划问题
# 将重复性问题归纳规律

def climbStairs(self, n: int) -> int:
    s = [1, 2]
    for i in range(2, n):
        s.append(s[i - 1] + s[i - 2])
    return s[n - 1]