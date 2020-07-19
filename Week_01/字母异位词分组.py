#   排序后作为字典的key来存储
#   可以直接将sorted()返回的字符列表转为字符串作为key
#   也可以用join()函数连成字符串作为key
#   使用join()结果运行比较快，可能是key比较短，查找比较快

def groupAnagrams(self, strs):
    res = dict()
    for word in strs:
        key = "".join(sorted(word))
        if key in res:
            res[key].append(word)
        else:
            res[key] = [word]
    return list(res.values())


def groupAnagrams(self, strs):
    dict = {}
    for item in strs:
        key = tuple(sorted(item))
        dict[key] = dict.get(key, []) + [item]
    return list(dict.values())
