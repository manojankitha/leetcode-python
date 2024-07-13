#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output:List[int] = []
        # create a dict 
        map:dict[int,int] = {}
        # here were traverse through the array O(n)
        for i in range(len(nums)):
            if nums[i] in map:
                output = [i,map[nums[i]]]
                break  
            else:
                # store the number we want to find as key of map and the index we already have as value so we can use later
                map[target-nums[i]] = i
        return output
 
# TC: O(n) for traversing the array of length n
# SC: O(n) for the map and nums of length n
# @lc code=end
