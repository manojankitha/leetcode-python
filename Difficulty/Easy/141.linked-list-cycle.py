#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while(fast!=None and fast.next!=None):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                return True
        return False
    
# TC: O(n) where n is #nodes in linked list
# SC: O(1) constant space

# @lc code=end

