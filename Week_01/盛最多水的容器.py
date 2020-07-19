# 思路是双指针，往中间滑动，动态存储比较面积（较短边乘两边距离）

def maxArea(self, height) -> int:
    l,r,res=0,len(height)-1,0
    while l<r:
        if height[l]<height[r]:
            res=max(res,height[l]*(r-l))
            l+=1
        else:
            res=max(res,height[r]*(r-l))
            r-=1
    return res