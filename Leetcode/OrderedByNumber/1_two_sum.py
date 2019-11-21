# -*- coding: utf-8 -*-
"""
- File Name: 1_two_sum
- Description: 
- Author: qi
- Create Date: 7/19/19
- Change Activity: 
                   7/19/19: First edit.
- Announcement: All rights reserved by qi.
                Use Apache License.
 
"""
__author__ = 'qi'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, e in enumerate(nums):
            for j in range(i+1, len(nums)):
                if e+nums[j] == target:
                    return [i, j]
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15, 99, -1, 9, 20, -1, 20]
    target = 19
    ans = Solution().twoSum(nums, target)
    print(ans)
