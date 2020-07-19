# k对nums长度求余数，剩下的就是需要移动的数量
# 先将数组反转
# 把前k个值反转
# 把剩余值反转


def rotate(self, nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]

# 或者不需反转列表，直接把后半段和前半段的重新拼接
# nums[:] = nums[n-k:] + nums[:n-k]



#  有一个困惑，之前尝试用双向列表，然后用 rotate方法转k，但是输出总是原始输入
#  q=collections.deque(nums)
#  q.rotate(k)

# 希望老师帮忙解惑