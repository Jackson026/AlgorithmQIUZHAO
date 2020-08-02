
# 1.定义步数step=0，能达到的最远位置max_bound=0，和上一步到达的边界end=0。
# 2.遍历数组，遍历范围[0,n-1)：
    # A.所能达到的最远位置max_bound=max(max_bound,nums[i]+i)，表示上一最远位置和当前索引i和索引i上的步数之和中的较大者。
    # B.如果索引i到达了上一步的边界end，即i==end，则：
    #   b1.更新边界end，令end等于新的最远边界max_bound，即end=max_bound
    #   b2.令步数step加一
# 3.返回step
# **注意！**数组遍历范围为[0,n-1)，因为当i==0时，step已经加一,所以若最后一个元素也遍历的话，当end恰好为n−1，步数会多1

def jump(self, nums) -> int:
    step=0
    end=0
    max_bound=0
    for i in range(len(nums)-1):
        max_bound=max(max_bound,nums[i]+i)
        if(i==end):
            step+=1
            end=max_bound
    return step