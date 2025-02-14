'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''


class Solution(object):
    def mergeTwoLists(self, list1: list, list2: list):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        result = []

        while list1 and list2:
            m = min(list1[0], list2[0])
            result.append(m)
            try:
                list1.remove(m)
            except Exception:
                list2.remove(m)

        result.extend(list1)
        result.extend(list2)

        return result


# x = Solution()
# print(x.mergeTwoLists(list1=[1,2,4], list2=[1,3,4]))


