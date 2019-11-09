# -*- coding: utf-8 -*-
"""
Created on =2019-11-09

@author: wenshijie
"""
import time


class Solution:
    def generateParenthesis(self, n: int) -> list:
        if n == 0:
            return []
        result = []

        def gp(s: str, d: list):
            """
            :param s: 当前字符串
            :param d: 当前所剩的[(,)]的数量
            :return:
            """
            if d[1] == 0:
                result.append(s)
            if d[1] >= d[0] - 1 >= 0:
                gp(s + '(', [d[0] - 1, d[1]])
            if d[1] - 1 >= 0 and d[1] - 1 >= d[0]:
                gp(s + ')', [d[0], d[1] - 1])

        gp('', [n, n])
        return result


if __name__ == '__main__':
    S = Solution()
    st = time.time()
    print(S.generateParenthesis(10))
    en = time.time()
    print(en - st)
