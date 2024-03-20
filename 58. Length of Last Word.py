# region description
'''
https://leetcode.com/problems/length-of-last-word/description/
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
# endregion

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        ml = s.split()
        return len(ml[-1])
        '''
        s = s.rstrip()
        space_index = s.rfind(' ')
        # если пробела нет в строке, rfind вернет -1
        if space_index == -1:
            return len(s)
        return len(s) - space_index - 1

# region BEST solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length 
# endregion