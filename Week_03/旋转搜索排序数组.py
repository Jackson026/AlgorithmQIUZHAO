
# 套用二分法

def search(self, nums, target: int) -> int:
    if len(nums) <= 0:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (r - l) // 2 + l
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[l]:
            if nums[l] <= target <= nums[mid]:
                r = mid
            else:
                ''' 这里 +1，因为上面是 <= 符号 '''
                l = mid + 1
        else:
            '''注意：这里必须是 mid+1，因为根据我们的比较方式，mid属于左边的序列'''
            if nums[mid + 1] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid
    return l if nums[l] == target else -1