'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    # def threeSum(self, nums):
    #     if nums.__len__() < 3:
    #         return []
    #
    #     numsAmountMap = dict()
    #     for n in nums:
    #         if n in numsAmountMap:
    #             numsAmountMap[n] += 1
    #         else:
    #             numsAmountMap[n] = 1
    #
    #     keyList = list(numsAmountMap.keys())
    #     keyList.sort()
    #
    #     outputList = list()
    #
    #     for idxI, i in enumerate(keyList):
    #         if i > 0:
    #             return outputList
    #         for idxJ, j in enumerate(keyList[(idxI if numsAmountMap[i] > 1 else idxI + 1):]):
    #             firstTwoSum = i + j
    #             if firstTwoSum > 0:
    #                 continue
    #             thirdNum = 0 - firstTwoSum
    #             idxJ = keyList.index(j)
    #             if thirdNum in keyList[(idxJ if numsAmountMap[j] > 1 else idxJ + 1):]:
    #                 if (thirdNum == 0 and numsAmountMap[0] < 3) or (thirdNum == j and numsAmountMap[thirdNum] < 2):
    #                     break
    #                 outputList.append([i, j, thirdNum])
    #
    #     return outputList
    def threeSum(self, nums):
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
                if threeNumsSum < 0:
                    idxLeftNum += 1
                elif threeNumsSum > 0:
                    idxRightNum -= 1
                elif threeNumsSum == 0:
                    idxLeftNum += 1
                    idxRightNum -= 1
                    if not (outputList.__len__() > 0 and [fixedNumber, leftNum, rightNum] == outputList[-1]):
                        outputList.append([fixedNumber, leftNum, rightNum])

                leftNum = nums[idxLeftNum]
                rightNum = nums[idxRightNum]

        return outputList


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1, -1, 2], [-1, 0, 1]]
    print(s.threeSum([-1,0,1,0])) # [[-1, 0, 1]]
    print(s.threeSum([3,0,-2,-1,1,2])) # [[-2,-1,3],[-2,0,2],[-1,0,1]]
    print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])) # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
    print(s.threeSum([0,0,0])) # [[0,0,0]]
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])) # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
