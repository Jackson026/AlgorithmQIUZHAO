
# 1.排序数组
# 2.比较胃口与饼干

# g：孩子的胃口值
# s：饼干的尺寸
def findContentChildren(self, g, s) -> int:
    sl = sorted(s)
    gl = sorted(g)
    si, gi = 0, 0
    while si < len(s) and gi < len(g):
        if gl[gi] <= sl[si]:
            gi += 1
        si += 1
    return gi