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
        for i in range(n - 2):
            l, r = i + 1, n - 1
            if nums[i] > 0:  # 大于0时说明后面的相加已经不可能等于0了
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 避免首值重复的可能如[-4,-4,-2,-2,1,0,5,6,6]中[-4,-2,-6]中的-4
                continue
            while l < r:
                if sum([nums[i], nums[l], nums[r]]) == 0:
                    # 避免首个相同,其余两个值重复如[-4,-4,-2,-2,1,0,5,6,6]中[-4,-2,-6]
                    if not ((l - 1 > i and nums[l] == nums[l - 1]) or (r < n - 1 and nums[r] == nums[r + 1])):
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1  # r-=1小的增加，或大的减小都可以
                elif sum([nums[i], nums[l], nums[r]]) < 0:  # 和小于0，此时r已经是最大的可能，所以只能增加l
                    l += 1
                else:
                    r -= 1
        return result


if __name__ == "__main__":
    nums = [-4, -4, -2, -2, -1, 0, 5, 6, 6]
    S = Solution()
    print(S.threeSum(nums))
