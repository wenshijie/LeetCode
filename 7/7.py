# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:52:03 2019

@author: lenovo
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return '0'
        s = str(x)
        pos = ''
        if s[0] =='-':
            pos = '-'
            s = s[1:]
        i = -1
        while s[i]=='0':
            s = s[:i]
        if pos:
            return pos+s[::-1]
        return s[::-1]
        

if __name__ == "__main__":
    x=10
    S = Solution()
    print(S.reverse(x))