
# 从后往前更新位置，如果前一个位置可以跳到end,就把end坐标换成前一个的
# 终止条件为坐标为0

def canJump(self, nums) -> bool:
    if not nums:
        return 0
    end_position = len(nums) - 1
    for i in range(end_position - 1, -1, -1):
        if nums[i] + i >= end_position:
            end_position = i
    return end_position == 0