# region description
'''
https://leetcode.com/problems/container-with-most-water/description/
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
'''
# endregion


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # решение за O(N**2)
        # ma = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         mini = min(height[i], height[j])
        #         cur_ma = mini * (j - i)
        #         ma = max(ma, cur_ma)
        # return ma

        L = 0
        R = len(height) - 1
        ma = 0
        while R > L:
            mini = min(height[L], height[R])
            cur_ma = mini * (R - L)
            ma = max(ma, cur_ma)
            if height[L] >= height[R]:
                R -= 1
            else:
                L += 1

        return ma



# x = Solution()
# print(x.maxArea([1,8,6,2,5,4,8,3,7]))