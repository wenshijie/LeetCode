# -*- coding: utf-8 -*-
"""
Created on =2019-11-09

@author: wenshijie
"""


class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        dict_ = dict(zip((')', ']', '}'), ('(', '[', '{')))
        for i in s:
            if i in ('(', '[', '{'):
                result.append(i)
            if i in (')', ']', '}'):
                if not result:
                    return False
                elif result[-1] == dict_[i]:
                    del result[-1]
                else:
                    return False
        return not result


if __name__ == "__main__":
    s = "{[]}"
    S = Solution()
    print(S.isValid(s))
