"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum_num = 0
        accumulated_num = 0

        for num in nums:
            if num == 0:
                maximum_num = max(maximum_num, accumulated_num)
                accumulated_num = 0
            else:
                accumulated_num += 1

        return max(maximum_num, accumulated_num)


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))

    nums = [1,0,1,1,0,1]
    print(Solution().findMaxConsecutiveOnes(nums))
