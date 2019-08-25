# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:45:11 2019

@author: lenovo
"""
x = 3
target = 365
num = -1
res = target%x  # 余数
target = target//x  # 商
if res<=x/2:
    num += res*2
else:
    num += (x-res)*2+1
    target = target+1

k = 0
while target !=0:
    print(target)
    print(num)
    res = target%x
    target = target//x
    if target!=0:
        if res==0:
            pass 
        elif res <=x/2 and res >0:  # 余数小于分母的一半
            num += k+1
        else:
            target = target+1
            num += k+1
        k +=1
    else:
        if res <=x//2+1:
            num += (k+1)*res
        else:
            num += (k+1)*(x-res+1)+1
    

'''
while target>0:
    if target>=x:
        num = 0
        x1 = x
        while target>=x1:
            x1 *= x
            num += 1
        if target*x//x1<=x//2+1:
            num = num
            target = target - x1/x
        else :
            num = num+1
            target = x1-target
    else :   
        if target<=x/2:
            num = target*2
        else:
            num = (x-target)*2+1
        target = 0
    print(target)
    print(num)
    result +=num
'''
#[[3,19,5],[3,365,17],[100,100000000,3],[5,501,8],[3,929,19]]