# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/remove-element/
'''

###############################################


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)


###############################################
s = Solution()

arr = [0, 1, 2, 0, 1, 2]
result = s.removeElement(arr, 2)

print(result)
