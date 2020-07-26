
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 回溯算法


def combine(self, n: int, k: int):
    if n < k:
        return []
    res = []

    def backtrack(l, k, t):
        if k == 0:
            res.append(t)
            return
        for i in range(l, n + 1):
            backtrack(i + 1, k - 1, t + [i])

    backtrack(1, k, [])
    return res


#直接使用库

import itertools

def combine(self, n: int, k: int):
    return list(itertools.combinations(range(1, n + 1), k))