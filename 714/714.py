# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:04:52 2019

@author: lenovo
"""
# 没想到其它方法
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
    
