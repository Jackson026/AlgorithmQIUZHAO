# 方法1
# 先判断两个字符串不重复的字符数是否一致
# 再判断每个字符在原本字符串的数量是否一致

def isAnagram(self, s: str, t: str) -> bool:
    # return True if sorted(s)==sorted(t) else False
    if len(s) != len(t):
        return False
    se = set(s)
    if se == set(t):
        for i in se:
            if s.count(i) != t.count(i):
                return False
        return True
    else:
        return False


# 方法2
# 直接比较两个字符串排序后的值是否一致，一行代码

def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s)==sorted(t) else False