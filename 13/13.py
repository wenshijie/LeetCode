# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:20:55 2019

@author: lenovo
"""

#  罗马转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        k_v = {'M': 1000, 'C': 100, 'X': 10, 'I': 1, 
               'D': 500, 'L': 50, 'V': 5}
        i, n = 0, len(s)
        result = 0
        while i<n:
            if i+1<n and k_v[s[i]]<k_v[s[i+1]]:
                result += k_v[s[i+1]]-k_v[s[i]]
                i+=2
            else:
                result += k_v[s[i]]
                i+=1
        return result    
if __name__ == "__main__":
    s = "III"
    S=Solution()
    print(S.romanToInt(s))