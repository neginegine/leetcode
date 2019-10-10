# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/friend-circles/
'''

###############################################


class Solution(object):

    def circle_root(self, circle_indexs, index):
        while circle_indexs[index] != index:
            index = circle_indexs[index]
        return index

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circle_indexs = list()

        for i in range(len(M)):
            circle_indexs.append(i)

        for i in range(len(M)):
            for j in range(i + 1, len(M[0])):
                if M[i][j] == 1:
                    if circle_indexs[j] == j:
                        circle_indexs[j] = circle_indexs[i]
                    else:
                        root_i = i
                        root_j = j

                        while circle_indexs[root_i] != root_i:
                            root_i = circle_indexs[root_i]
                        while circle_indexs[root_j] != root_j:
                            root_j = circle_indexs[root_j]

                        circle_indexs[i] = root_i
                        circle_indexs[j] = root_i
                        circle_indexs[root_j] = root_i

        circle_count = 0

        for i in range(len(M)):
            if circle_indexs[i] == i:
                circle_count += 1
        return circle_count


###############################################
s = Solution()

M = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 1, 0, 0, 0, 0, 1, 1]]


# 0 3 6 5 1 8 9
# 2
# 4

print(s.findCircleNum(M))
