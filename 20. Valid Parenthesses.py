'''
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        expected = []
            
        dct = {'(': 0,
               '[': 0,
               '{': 0,
               ')': 0,
               ']': 0,
               '}': 0}
        
        dct2 = {'(': ')',
                '[': ']',
                '{': '}'}
        
        for char in s:
            if char in ('([{'):
                expected.append(dct2[char])
            else:
                if expected:
                    if expected[-1] != char:
                        return False
                    else:
                        expected.pop()
                else:
                    return False

            dct[char] += 1

            # if dct['('] - dct[')'] < 0 or dct['['] - dct[']'] < 0 or dct['{'] - dct['}'] < 0:
            #     return False
            
        return dct['('] == dct[')'] and dct['['] == dct[']'] and dct['{'] == dct['}']
            
x = Solution()
print(x.isValid('[([]])'))


