# 取巧的办法是转换成字符串然后变为int，最后再转换回去原来的形式，通用性不强，就不作为一种方法写在这里

# 按位运算，倒序，如果是9，就变为0，向前循环，不为9则直接加1；
# 如果为999这种特殊形式，则在循环结束后，列表头插入1 .insert(位置，数)
def plusOne(self, digits):
    if not digits:
        return digits + [1]
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            break
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits