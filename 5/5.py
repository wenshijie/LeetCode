# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:55:10 2019

@author: lenovo
"""
# 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        res_index = [0,1]  # 初始为第一个元素，回文数为 1
        res = 1
        num = 0
        for i in range(1,n-1):  # 奇数回文时
            if s[i-1]==s[i+1]:
                num, k = 3, 2
                result = [i-1,i+2]
                while i-k>-1 and i+k<n:
                    if s[i-k]==s[i+k]:
                        num += 2
                        result =[i-k,i+k+1]
                        k += 1
                    else:
                        break
            if num>res:
                res = num
                res_index=result.copy()
        for i in range(n-1):  # 偶数回文时
            if s[i]==s[i+1]:
                num, k = 2, 2
                result = [i,i+2]
                while i-k+1>-1 and i+k<n:
                    if s[i-k+1]==s[i+k]:
                        num += 2
                        result = [i-k+1,i+k+1]
                        k += 1
                    else:
                        break
            if num>res:
                res = num
                res_index=result.copy()
        return s[res_index[0]:res_index[1]]
                
if __name__ == "__main__":
    # bb aaaa 
    s='abc'
    S=Solution()
    print(S.longestPalindrome(s))
           