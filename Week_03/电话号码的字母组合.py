
# 回溯
# digits是数字字符串

phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

def letterCombinations(self, digits: str):
    def dfs(s, d):
        if len(d) == 0:
            res.append(s)
            return
        for i in phone[d[0]]:
            dfs(s + i, d[1:])


    res = []
    if digits:
        dfs('', digits)
    return res