"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        start_num = nums[0]
        end_num = nums[0]
        range_list = []

        for i, num in enumerate(nums[1:]):
            if end_num + 1 == num:
                end_num = num
            else:
                if start_num == end_num:
                    range_list.append(f"{start_num}")
                else:
                    range_list.append(f"{start_num}->{end_num}")
                start_num = num
                end_num = num


        if start_num == end_num:
            range_list.append(f"{start_num}")
        else:
            range_list.append(f"{start_num}->{end_num}")

        return range_list


if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))

    nums = [0,2,3,4,6,8,9]
    print(Solution().summaryRanges(nums))

    nums = []
    print(Solution().summaryRanges(nums))

    nums = [1]
    print(Solution().summaryRanges(nums))
