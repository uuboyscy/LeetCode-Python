"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
"""Boyer-Moore voting algorithm"""
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # len(nums) / 2
        majority = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                majority = num
            count += 1 if majority == num else -1

        return majority


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(
        Solution().majorityElement(nums)
    )
