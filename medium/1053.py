# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/previous-permutation-with-one-swap/
'''

###############################################


class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        i = len(A) - 2
        while i > -1 and A[i] <= A[i + 1]:
            i -= 1

        if i < 0:
            return A

        num_i = A[i]

        j = len(A) - 1
        while j > i and num_i <= A[j]:
            j -= 1

        num_j = A[j]

        while j - 1 > i and num_j == A[j - 1]:
            j -= 1

        A[i] = num_j
        A[j] = num_i

        return A


###############################################
s = Solution()

result = s.prevPermOpt1([3, 1, 1, 3])

print(result)
