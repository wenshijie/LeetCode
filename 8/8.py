# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:45:33 2019

@author: lenovo
"""
# 
class Solution:
    def myAtoi(self, str: str) -> int:
        n = len(str)
        i = 0
        while i<n:
            if str[i]==' ':
                i+=1
                continue
            elif str[i]=='-' or str[i]=='+' or str[i].isdigit():
                pos=str[i]
                num = ''
                while i+1<n:
                    if str[i+1].isdigit():
                        num+=str[i+1]
                        i+=1
                    else:
                        break
                if pos.isdigit():
                    num=pos+num
                while len(num)>0 and num[0]=='0':
                    num = num[1:]
                if num=='':
                    return 0
                elif int(num)<2147483648:
                    return '-'+num if pos=='-' else num
                else:
                    return '-'+'2147483648' if pos=='-' else '2147483647'
            else:
                return 0
        return 0
    
if __name__ == "__main__":
    s="  0000000000012345678"
    S = Solution()
    print(S.myAtoi(s))
