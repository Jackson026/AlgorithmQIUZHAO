
# 因为多数元素定义，必然超过数组长度的一半，所以我们排序后，取出数组中间位置的值，该值必为多数元素

def majorityElement(self, nums) -> int:
    nums.sort()
    return nums[len(nums) // 2]


# 分治法

def majorityElement(self, nums, lo=0, hi=None):
    def majority_element_rec(lo, hi):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice.
        mid = (hi - lo) // 2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)

# 摩尔投票，一次遍历

def majorityElement(self, nums) -> int:
    count, major = 0, 0
    for n in nums:
        if count == 0:
            major = n
        if n == major:
            count += 1
        else:
            count -= 1
    return major