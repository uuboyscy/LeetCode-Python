"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        n = 1
        while n < k:
            heapq.heappop(nums)
            n += 1

        return -heapq.heappop(nums)


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums, k))
