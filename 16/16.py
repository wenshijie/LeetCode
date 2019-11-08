# -*- coding: utf-8 -*-
"""
Created on =2019-11-07

@author: wenshijie
"""


# 最接近的三数之和
# 减去两个之和求距离第三个值最近的值
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        n = len(nums)
        distance = float("inf")
        if n < 3:
            return 0
        for i in range(n - 2):
            for j in range(i+1,n-1):
                find = target - nums[i] - nums[j]
                left, right = j+1, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == find:
                        return target
                    elif nums[mid] > find:
                        right = mid
                    else:
                        left = mid
                    if right - left < 2:
                        if min(abs(nums[left] - find), abs(nums[right] - find)) < distance:
                            distance = min(abs(nums[left] - find), abs(nums[right] - find))
                            if abs(nums[left] - find) < abs(nums[right] - find):
                                result = target - find + nums[left]
                            else:
                                result = target - find + nums[right]
                        break
        return result


if __name__ == "__main__":
    nu = [-4,-1,1,2]#[-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
    ta = 1
    S = Solution()
    print(S.threeSumClosest(nu, ta))
