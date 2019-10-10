# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/duplicate-zeros/
'''

###############################################


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()


###############################################
s = Solution()

arr = [0, 1, 2, 0, 1, 2]
s.duplicateZeros(arr)

print(arr)
