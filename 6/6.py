# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:52:12 2019

@author: lenovo
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        result = ''
        if n<=numRows or numRows==1:
            return s
        for k in range(numRows):
            result += s[k]
            max_ = 2*(numRows-1)-2*k
            min_ = 2*k
            while k<n:                               
                k += max_
                if max_>0 and k<n:
                    result+=s[k]
                k += min_
                if min_>0 and k<n:
                    result+=s[k]
        return result
                
                

if __name__ == "__main__":
    s = ""
    numRows = 1
    S = Solution()
    print(S.convert(s,numRows))