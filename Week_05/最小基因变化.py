class Solution:
    ## start: str, end: str, bank: List[str]
    def minMutation(self, start: str, end: str, bank) -> int:

        # from collections import deque
        # bank = set(bank)
        # if end not in bank:
        #     return -1
        # visited = set()
        # visited.add(start)
        # mutation = {"A", "C", "G", "T"}

        # # 产生只差一个字母的基因
        # def oneMutation(cur):
        #     for i, val in enumerate(cur):
        #         for t in mutation - {val}:
        #             tmp = cur[:i] + t + cur[i + 1:]
        #             if tmp in bank:
        #                 yield tmp

        # queue = deque()
        # queue.appendleft([start, 0])
        # while queue:
        #     cur, res = queue.pop()
        #     if cur == end:
        #         return res
        #     for nxt in oneMutation(cur):
        #         if nxt not in visited:
        #             visited.add(nxt)
        #             queue.appendleft((nxt, res + 1))
        # return -1

        # 和单词搜索题目基本一致，可以参考
        stack=[[start,0]]
        bankset=set(bank)
        while stack:
            word,step=stack.pop(0)
            if word==end:
                return step
            for i in range(len(start)):
                for l in "AGCT":
                    new_word=word[:i]+l+word[i+1:]
                    if new_word in bankset:
                        bankset.remove(new_word)
                        stack.append([new_word,step+1])
        return -1