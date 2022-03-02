"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

List = list

class Solution:

    def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
        if nums.__len__() < 3:
            return []

        outputList = []
        nums.sort()
        numsSet = set(nums)

        for fixedNumber in numsSet:
            idxLeftNum = nums.index(fixedNumber) + 1
            idxRightNum = nums.__len__() - 1
            if idxLeftNum > nums.__len__() - 2: continue
            leftNum = nums[idxLeftNum]
            rightNum = nums[idxRightNum]
            while idxLeftNum < idxRightNum:
                threeNumsSum = fixedNumber + leftNum + rightNum
                if threeNumsSum < target:
                    idxLeftNum += 1
                elif threeNumsSum > target:
                    idxRightNum -= 1
                elif threeNumsSum == target:
                    idxLeftNum += 1
                    idxRightNum -= 1
                    if not (outputList.__len__() > 0 and [fixedNumber, leftNum, rightNum] == outputList[-1]):
                        outputList.append([fixedNumber, leftNum, rightNum])

                leftNum = nums[idxLeftNum]
                rightNum = nums[idxRightNum]

        return outputList

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums.__len__() < 4:
            return []

        outputList = []
        nums.sort()
        numsSet = set(nums)

        for fixedNumber in numsSet:
            idx = nums.index(fixedNumber) + 1
            outputList += [[fixedNumber] + threeList for threeList in self.threeSum(nums[idx:], target - fixedNumber)]


        return outputList


if __name__ == '__main__':

    s = Solution()

    nums = [1,0,-1,0,-2,2]
    target = 0
    print(s.fourSum(nums, target)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums = [2,2,2,2,2]
    target = 8
    print(s.fourSum(nums, target))  # [[2,2,2,2]]

