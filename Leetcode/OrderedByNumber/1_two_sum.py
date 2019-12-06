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
    # Brute Force
    def twoSumStraight(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, e in enumerate(nums):
            for j in range(i+1, len(nums)):  # expcept self需要排除自身
                if e+nums[j] == target:
                    return [i, j]
        return None

    # Brute Force
    # Success
    # Details 
    # Runtime: 3276 ms, faster than 27.66% of Python online submissions for Two Sum.
    # Memory Usage: 12.4 MB, less than 95.89% of Python online submissions for Two Sum.
    def twoSumBruteForce(self, nums, target):
        for i, e in enumerate(nums):
            complete = target - e
            for j in range(i+1, len(nums)):
                if complete == nums[j]:
                    return [i, j]
        return None

    # Hash table / search table
    # Success
    # Details 
    # Runtime: 1940 ms, faster than 29.26% of Python online submissions for Two Sum.
    # Memory Usage: 13.3 MB, less than 14.04% of Python online submissions for Two Sum.
    def twoSumTwoPassHash(self, nums, target):
        tbl = {}
        # construct a search table
        for i, e in enumerate(nums):  # what if there are same elements?
            tbl[e] = i
        # search
        for i, e in enumerate(nums):
            complete = target - e
            if complete in tbl.keys() and i!=tbl[complete]:
                return [i, tbl[complete]]
            # else continue
    
    # twoSumOnePassHash
    # Success
        # Details 
        # Runtime: 652 ms, faster than 38.67% of Python online submissions for Two Sum.
        # Memory Usage: 13.2 MB, less than 22.26% of Python online submissions for Two Sum.
    def twoSum(self, nums, target):
        tbl = {}
        for i, e in enumerate(nums):
            complete = target - e

            if complete not in tbl.keys():
                tbl[e] = i
            else:
                return [tbl[complete], i]
            
            

if __name__ == '__main__':
    nums, target = [2, 7, 11, 15, 99, -1, 9, 20, -1, 20], 19
    # case1: [3, 2, 2, 4]  6  ans1: [1, 2]
    nums, target = [3, 2, 4], 6
    ans = Solution().twoSum(nums, target)
    print(ans)


