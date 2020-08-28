'''
从前往后遍历字符串
一、入栈条件为1.栈为空 2.当前字符是'(' 3.栈顶符号位')'，因为三种条件都没办法消去成对的括号。
二、计算结果：符合消去成对括号时，拿当前下标减去栈顶下标即可
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans