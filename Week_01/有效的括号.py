def isValid(self, s: str) -> bool:
    stack=["?"]
    mapping = {"(": ")", "[": "]", "{": "}", "?": "?"}
    for i in s:
        if i in mapping:
            stack.append(i)
            continue
        elif mapping[stack.pop()]!=i:
            return False

    return len(stack) ==1

# 字典存好三种括号，键值对