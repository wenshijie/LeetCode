# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:45:56 2019

@author: lenovo
"""

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ''
        n = min(list(map(len,strs)))
        if n == 0:
            return ''
        i = -1
        switch = True
        while i<n-1 and switch:
            i+=1
            for item in strs:
                if item[i]!=strs[0][i]:
                    switch = False
        return strs[0][:n] if switch else strs[0][:i] 
    
if __name__ == "__main__":
    strs =['aa','a']# ["flower","flow","flight"]  # [] [""] ['aa','a']
    S = Solution()
    print(S.longestCommonPrefix(strs))