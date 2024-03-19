'''
https://leetcode.com/problems/find-the-pivot-integer/description/
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1.
It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
'''

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = int(n * 0.7)
        flag = None

        while True:

            left_sum = sum(range(1, start + 1))
            right_sum = sum(range(start, n + 1))
            
            if left_sum == right_sum:
                return start

            elif left_sum < right_sum:
                # проверяем, была ли раньше больше левая часть
                if flag == 'left':
                    return -1

                flag = 'right'
                start += 1


            elif left_sum > right_sum:
                # проверяем, была ли раньше больше правая часть
                if flag == 'right':
                    return -1

                flag = 'left'
                start -= 1


        