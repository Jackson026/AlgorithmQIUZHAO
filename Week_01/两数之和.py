#使用字典完成任务，O(N)的时间、空间复杂度
def twoSum(nums, target: int):
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:  # 判断的是key是否在dic中
            return [nums.index(target - num), i]
        dic[num] = i

