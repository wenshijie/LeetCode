# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:25:38 2019

@author: lenovo
"""

import itertools
points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
points = set(map(tuple, points))
ans = float('inf')
for p1, p2, p3 in itertools.permutations(points,3):
    p4 = (p1[0]+p3[0]-p2[0], p1[1]+p3[1]-p2[1])  # p2为交点
    if p4 in points:
        v1 = complex(p2[0]-p1[0],p2[1]-p1[1])
        v2 = complex(p2[0]-p3[0],p2[1]-p3[1])
        if v1.real*v2.real+v1.imag*v2.imag==0:
            area = abs(v1)*abs(v2)
            if area<ans:
                ans = area
result = ans if ans<float('inf') else 0