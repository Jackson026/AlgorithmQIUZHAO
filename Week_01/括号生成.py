def generateParenthesis(self, n: int):
    res = []

    def dfs(left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            dfs(left - 1, right, path + '(')
        if left < right:
            dfs(left, right - 1, path + ')')

    dfs(n, n, '')
    return res



# 生成所有可能的合法的括号对
# 通过递归解决问题
# 其中两个要素：1 左边的括号要比右边的多，此时可以增加右括号 2 插入数量不超过n
# 流程：
# 写一个函数，参数为 字符串（记录最终输出）、左括号、右括号
# 终止条件：左右括号都用完，res加入生成括号
# 左边括号数大于0，加（
# 右边括号多于左边括号，加 ）