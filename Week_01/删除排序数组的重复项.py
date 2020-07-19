def removeDuplicates(nums):
    if not nums:
        return 0
    for i in range(len(nums)-1,0,-1):
        if nums[i]==nums[i-1]:
            nums.pop(i)
    return len(nums)

nums=[1,1,2,4,5,5]

print(removeDuplicates(nums))



#从头到位遍历的话，边界不好控制，所以可以选择反向遍历，如果前一个数与当前数值相同，就删除当前数
#最后返回剩余列表的长度，且所有操作在原数组上实现