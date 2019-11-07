# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:35:30 2019

@author: lenovo
"""
# 1 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i= 0
        n = len(s)
        result = 0
        while i<n:
            j = i+1
            res = 1
            while j<n:
                if s[j] in s[i:j]:
                    break
                j += 1
                res += 1
            result = max(result,res)
            i += 1
        return result
"""
# 窗口法

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vector = ''
        result, m = 0, 0
        n = len(s)
        i = 0
        while i<n:
            j = 0
            while j<m:
                if s[i]==vector[j]:
                    vector=vector[j+1:]
                    break
                j+=1
            vector += s[i]
            m = len(vector)
            result = max(result,m)
            i += 1
        return result
            