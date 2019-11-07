# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:33:00 2019

@author: lenovo
"""


#  三数之和
class Solution:
    def threeSum(self, nums: list) -> list:
        n = len(nums)
        if len(nums) < 3:
            return []
        nums.sort()
        result = []

        def tsm(i, value, res):
            if len(res) == 3:
                if value == 0:
                    result.append(res)
            else:
                if i < n - 1 and value + nums[i + 1] <= 0:
                    tsm(i + 1, value + nums[i + 1], res + [nums[i + 1]])

                    tsm(i + 1, value, res)

        tsm(-1, 0, [])
        return [list(re) for re in set(map(tuple, result))]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4, 4]
    S = Solution()
    print(S.threeSum(nums))
