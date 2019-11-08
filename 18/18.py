# -*- coding: utf-8 -*-
"""
Created on =2019-11-08

@author: wenshijie
"""


# 四数之和
class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        result = []
        for i in range(n - 3):
            if nums[i] > target / 4:  # 大于目标值的四分之一后面无可能
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 去除首个值重复的情况
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 去除第二个值重复的情况
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    if sum([nums[i], nums[j], nums[left], nums[right]]) == target:
                        if not ((left - 1 > j and nums[left] == nums[left - 1]) or (
                                right + 1 < n and nums[right] == nums[right + 1])):
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif sum([nums[i], nums[j], nums[left], nums[right]]) > target:
                        right -= 1
                    else:
                        left += 1
        return result


if __name__ == "__main__":
    nu = [1, 0, -1, 0, -2, 2]#[1, 0, 1, 2, -1, -1, 3, -3, -3, -3, 0, -1, 0, -2, 2]
    print(sorted(nu))
    ta = 0
    S = Solution()
    print(S.fourSum(nu, ta))
