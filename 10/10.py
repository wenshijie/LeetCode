# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:55:02 2019

@author: lenovo
"""
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0],'.'}
        if len(p)>1 and p[1]=='*':
            return (self.isMatch(s,p[2:]) or 
                    first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def match(i,j):
            if (i,j) not in dp:
                if j==len(p):
                    res = i==len(s)
                else:
                    first_match = i<len(s) and p[j] in {s[i],'.'}
                    if j<len(p)-1 and p[j+1]=='*':
                        res = match(i,j+2) or first_match and match(i+1,j)
                    else:
                        res = first_match and match(i+1,j+1)
                dp[i,j] = res
            return dp[i,j]
        return match(0, 0)

class Solution3(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        print(dp)

        return dp[0][0]


if __name__ == "__main__":
    s='aaa'
    p='aa*'
    S=Solution3()
    print(S.isMatch(s,p))        