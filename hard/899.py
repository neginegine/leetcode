# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/orderly-queue/submissions/
'''

###############################################


class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        chars = list(S)
        if K == 1:
            min_str = S
            for i in range(len(chars)):
                start_c = chars.pop(0)
                chars.append(start_c)
                tmp_str = "".join(chars)
                if tmp_str < min_str:
                    min_str = tmp_str
            return min_str
        else:
            chars.sort()
            return "".join(chars)


###############################################

s = Solution()

result = s.orderlyQueue("cba", 1)
print(result)

result = s.orderlyQueue("cbacdea", 3)
print(result)
