# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:30:13 2019

@author: lenovo
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m, n = len(nums1), len(nums2)
        if m>n:
            m, n,nums1, nums2 = n, m, nums2, nums1
        imin, imax,half = 0, m, (m+n+1)//2  # 左边应该有多少item,7->3,6->3
        while imin<=imax:
            i = (imin+imax)//2
            j = half-i              
            if i>0 and nums1[i-1]>nums2[j]:
                imax = i-1
            elif i<m and nums2[j-1]>nums1[i]:
                imin = i+1
            else:
                if i==0:
                    max_left=nums2[j-1]
                elif j==0:
                    max_left=nums1[i-1]
                else:
                    max_left=max(nums2[j-1],nums1[i-1])
                if (m+n)%2==1:
                    return max_left
                if i==m:
                    min_right = nums2[j]
                elif j==n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums2[j],nums1[i])
                return (max_left+min_right)/2

class Solution2:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m, n = len(nums1), len(nums2)
        k = (m+n-1)//2
        # 删除k个， 如果m+n为偶数结果为第一小和第二小的均值，否则取第一小
        #[1,2,3,4,5] ->[3,4,5] result->3
        #[1,2,3,4]->[2,3,4] result->(2+3)/2=2.5
        while k >0:
            if not nums1:  # nums1为空,直接从nums2中删除
                nums2=nums2[k:]
                k=0
            elif not nums2:  # nums2为空，直接从nums1中删除
                nums1=nums1[k:]
                k=0
            else:  # 否者按两数组中较小的一半值进行删除
                term = max(k//2,1)  #此次删除的个数 当k=1时，k//2=0也要删除1个
                if nums1[min(term-1,len(nums1)-1)]<nums2[min(term-1,len(nums2)-1)]:
                    # 取最小防止删除的个数大于列表长度，[1],[1,2,3,4,5]
                    # 在优先nums1中删除
                    if len(nums1)<=term:
                        # 如果nums1中剩余的个数小于要删除的个数
                        #则把nums1中的元素全删除，剩余的在nums2中删除
                        k = k-len(nums1)
                        nums1=[]
                        nums2 = nums2[k:]
                        k=0
                    else:
                        nums1 = nums1[term:]
                        k = k-term
                else:  # 在优先nums1中删除
                    if len(nums2)<=term:
                        # 如果nums2中剩余的个数小于要删除的个数
                        #则把nums2中的元素全删除，剩余的在nums1中删除
                        k = k-len(nums2)
                        nums2=[]
                        nums1 = nums1[k:]
                        k=0
                    else:
                        nums2 = nums2[term:]
                        k = k-term
        print(nums1,nums2)
        if not nums1:  # nums1为空
                return nums2[0] if (m+n)%2==1 else (nums2[0]+nums2[1])/2
        elif not nums2:  # nums2为空
            return nums1[0] if (m+n)%2==1 else (nums1[0]+nums1[1])/2
        else:
            if (n+m)%2==1:
                return min(nums1[0],nums2[0])
            else:
                if nums1[0]<=nums2[0]:
                    min1=nums1[0]
                    del nums1[0]
                    min2=min(nums1[0],nums2[0]) if nums1 else nums2[0]
                else:
                    min1=nums2[0]
                    del nums2[0]
                    min2=min(nums1[0],nums2[0]) if nums2 else nums1[0]
                return (min1+min2)/2
if __name__=='__main__':  
    nums1 = [1,2]
    nums2 = [3,4]
    S=Solution2()
    print(S.findMedianSortedArrays(nums1,nums2))