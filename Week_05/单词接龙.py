class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # 1.转换词列表放入set集合中
        # 2.把初始词和次数放入栈中
        # 3.遍历栈，pop出数据，每次遍历该词，判断转换字母后的词是否在转换词表里，如果在则对转换词表做剪枝

        wordset=set(wordList)
        stack=[[beginWord,1]]
        while stack:
            word,lenght=stack.pop(0)
            if word==endWord:
                return lenght
            for i in range(len(word)):
                for l in 'qazwsxedcrfvtgbyhnujmikolp':
                    new_word=word[:i]+l+word[i+1:]
                    if new_word in wordset and new_word!=word:
                        wordset.remove(new_word)
                        stack.append([new_word,lenght+1])
        return 0

        # def BFS(graph, start, end):
        #     visited = set()
        #     queue = []
        #     queue.append([start])
        #     while queue:
        #         node = queue.pop()
        #         visited.add(node)
        #         process(node)
        #         nodes = generate_related_nodes(node)
        #         queue.push(nodes)
        #     # other processing work
        #     # ...