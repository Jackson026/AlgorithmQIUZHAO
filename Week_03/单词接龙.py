class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # 1.转换词列表放入set集合中
        # 2.把初始词和次数放入栈中
        # 3.遍历栈，pop出数据，每次遍历该词，判断转换字母后的词是否在转换词表里，如果在则对转换词表做剪枝

        wordset=set(wordList)
        stack=[[beginWord,1]]
        while stack:
            word,length=stack.pop(0)
            if word==endWord:
                return length
            for i in range(len(word)):
                for letter in 'qazwsxedcrfvtgbyhnujmikolp':
                    new_word=word[:i]+letter+word[i+1:]
                    if new_word in wordset and new_word!=word:
                        wordset.remove(new_word)
                        stack.append([new_word,length+1])
        return 0