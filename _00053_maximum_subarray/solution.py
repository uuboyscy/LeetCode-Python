"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""
"""Kadane's algorithm"""
from math import inf


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -inf
        current_sum = 0
        for n in nums:
            current_sum = max(n, current_sum + n)
            max_sum = max(current_sum, max_sum)

        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(
        Solution().maxSubArray(nums)
    )