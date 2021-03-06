# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        current = 0
        result = nums[0]
        for i in nums:
            current += i
            result = max(current,result)
            current = max(0,current)
        return result
        

