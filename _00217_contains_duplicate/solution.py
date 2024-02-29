"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         num_count_map = {}
#         for num in nums:
#             if num in num_count_map:
#                 num_count_map[num] += 1
#             else:
#                 num_count_map[num] = 1

#         for v in num_count_map.values():
#             if v > 1:
#                 return True

#         return False


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         num_count_map = {}
#         for num in nums:
#             if num in num_count_map:
#                 return True
#             else:
#                 num_count_map[num] = 1

#         return False


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_count_set = set()
        for num in nums:
            if num in num_count_set:
                return True
            else:
                num_count_set.add(num)

        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))

    nums = [1,2,3,4]
    print(Solution().containsDuplicate(nums))

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containsDuplicate(nums))
