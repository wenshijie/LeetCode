# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:23:12 2019

@author: lenovo
"""
# 盛水最多

class Solution:
    def maxArea(self, height: list) -> int:
        res = 0
        n = len(height)
        for i in range(1,n):
            term = (n-i)*min(height[0],height[-1])
            res = term if term>res else res
            if height[0]<height[-1]:
                del height[0]
            else:
                del height[-1]
        return res


if __name__ == "__main__":
    height = [1,8,6]
    S = Solution()
    print(S.maxArea(height))
            