# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:44:18 2019

@author: lenovo
"""
# 回文数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]

if __name__ == "__main__":
    x=121
    S=Solution()
    print(S.isPalindrome(x))