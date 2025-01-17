#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List, Dict

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map:Dict[int,int] = {}
        for i in range(len(nums)):
            if nums[i] in map.keys():
                return True
            else:
                map[nums[i]]=1
        return False

# TC: O(n) for traversing the array of length n
# SC: O(n) for the map and nums of length n      
        
# @lc code=end

