class Solution:
    def canJump(self, nums) -> bool:
        # 从后往前更新位置，如果前一个位置可以跳到end,就把end坐标换成前一个的
        # 终止条件为坐标为0
        if not nums:
            return 0
        end=len(nums)-1
        for i in range(end-1,-1,-1):
            if nums[i]+i>=end:
                end=i
        return end==0