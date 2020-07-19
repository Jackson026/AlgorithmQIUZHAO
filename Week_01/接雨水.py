# 双指针解法
# 设置左右端点和左右最大值
# 持续更新两边最大值，如果是最大值，就用最大值减去左端值，并累加，否则就将新的端点值设为最大

def trap(self, height) -> int:
    if not height:
        return 0
    l, r, res = 0, len(height) - 1, 0
    lmax = height[l]
    rmax = height[r]
    while l < r:
        if height[l] < height[r]:
            if lmax > height[l]:
                res += lmax - height[l]
            else:
                lmax = height[l]
            l += 1
        else:
            if rmax > height[r]:
                res += rmax - height[r]
            else:
                rmax = height[r]
            r -= 1
    return res