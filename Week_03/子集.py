
# 回溯

# method1

def subsets(self, nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + r for r in res]
    return res

# method 2

def subsets(self, nums):
    res=[]
    def helper(i,t):
        res.append(t)
        for j in range(i,len(nums)):
            helper(j+1,t+[nums[j]])
    helper(0,[])
    return res