"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if not nums2:
            return []

        next_greater_element_dict = {}
        tmp_stack = [nums2[0]]

        for num in nums2[1:]:
            while tmp_stack and num > tmp_stack[-1]:
                next_greater_element_dict[tmp_stack[-1]] = num
                tmp_stack.pop()
            tmp_stack.append(num)

        for num in tmp_stack:
            next_greater_element_dict[num] = -1

        return [next_greater_element_dict[num] for num in nums1]


if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1, nums2))

    print("+++++")

    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(Solution().nextGreaterElement(nums1, nums2))
    print("+++++")

    nums1 = [1,3,5,2,4]
    nums2 = [5,4,3,2,1]
    print(Solution().nextGreaterElement(nums1, nums2))
    print("+++++")

    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    print(Solution().nextGreaterElement(nums1, nums2))
    print("+++++")

    nums1 = [1,3,5,2,4,6,7]
    nums2 = [6,5,4,3,2,1,7]
    print(Solution().nextGreaterElement(nums1, nums2))
    print("+++++")
