
# 套用二分法

def findMin(self, nums) -> int:
    if len(nums) == 1:
        return nums[0]
    l, r = 0, len(nums) - 1
    if nums[r] > nums[0]:
        return nums[0]
    while l <= r:
        mid = (r - l) // 2 + l
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[mid] > nums[0]:
            l = mid + 1
        else:
            r = mid - 1