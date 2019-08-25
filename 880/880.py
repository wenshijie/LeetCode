# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:43:35 2019

@author: lenovo
"""

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:        
        st, st_len='', 0
        st_s, st_l, st_long=[''], [0], [0]
        i= 0
        while i<len(S) and st_long[-1]<K:
            if S[i].isalpha():
                st += S[i]
                st_len += 1
            else:
                st_s.append(st)
                st_l.append(st_len)
                st_long.append((st_long[-1]+st_len)*int(S[i]))
                st, st_len='', 0
            i += 1
        if st_long[-1]<K:
            st_s.append(st)
            st_l.append(st_len)
            st_long.append(st_long[-1]+st_len)

        def find(k):   
            for i in range(len(st_s)-1):
                if k>st_long[i] and k<=st_long[i]+st_l[i+1]:
                    return st_s[i+1][k-st_long[i]-1]
                if k>st_long[i]+st_l[i+1] and k<=st_long[i+1]:
                    while k>st_long[i]+st_l[i+1]:
                        k = k-st_long[i]-st_l[i+1]
                    return find(k)
        return find(K)
            


