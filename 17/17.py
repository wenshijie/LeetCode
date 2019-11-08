# -*- coding: utf-8 -*-
"""
Created on =2019-11-07

@author: wenshijie
"""


# 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str) -> list:
        dict_ = dict(zip('23456789', map(list, ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'])))
        n = len(digits)
        if n == 0:
            return []
        result = ['']
        for i in digits:
            res = result.copy()
            result.clear()
            for item in res:
                for j in dict_[i]:
                    result.append(item + j)
        return result


if __name__ == "__main__":
    di = ''
    S = Solution()
    print(S.letterCombinations(di))
