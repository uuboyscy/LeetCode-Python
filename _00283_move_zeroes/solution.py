"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for idx, num in enumerate(nums):
            if num != 0:
                # tmp_num = nums.pop(idx)
                # nums.insert(non_zero_index, tmp_num)
                nums[idx] = 0
                nums[non_zero_index] = num
                non_zero_index += 1

        print(nums)


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for idx, num in enumerate(nums):
            if num != 0:
                tmp_num = nums.pop(idx)
                nums.insert(non_zero_index, tmp_num)
                non_zero_index += 1

        print(nums)




if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))

    nums = [0]
    print(Solution().moveZeroes(nums))
