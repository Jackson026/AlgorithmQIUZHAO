
#1.方法1，直接合并两个数组然后sort

def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    return sorted(nums1[:m]+nums2)

nums1=[1,3,4,0,0]
nums2=[1,2,5,5,6]
print(merge(nums1,3,nums2,5))


#方法2，双指针，从头比较两个数组的大小，哪个小，就先加到nums1中，最后多出来的直接添加

def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_n = nums1[:]
    nums1[:] = []
    l1, l2 = 0, 0
    while l1 < m and l2 < n:
        if nums1_n[l1] < nums2[l2]:
            nums1.append(nums1_n[l1])
            l1 += 1
        else:
            nums1.append(nums2[l2])
            l2 += 1
    if l1 < m:
        nums1[:] = nums1[:] + nums1_n[l1:m]
    if l2 < n:
        nums1[:] = nums1[:] + nums2[l2:n]


#方法3 倒序双指针
    def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m - 1
        l2 = n - 1
        p = m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] <= nums2[l2]:
                nums1[p] = nums2[l2]
                l2 -= 1
                p -= 1
            else:
                nums1[p] = nums1[l1]
                l1 -= 1
                p -= 1
        while l2 >= 0:
            nums1[p] = nums2[l2]
            l2 -= 1
            p -= 1