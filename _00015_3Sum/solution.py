'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums):
        if nums.__len__() < 3:
            return []
        # print(nums)

        numsAmountMap = dict()
        for n in nums:
            if n in numsAmountMap:
                numsAmountMap[n] += 1
            else:
                numsAmountMap[n] = 1

        keyList = list(numsAmountMap.keys())
        keyList.sort()

        # print(keyList)
        # print(numsAmountMap)

        outputList = list()

        for idxI, i in enumerate(keyList):
            if i > 0:
                # print(1)
                return outputList
            for idxJ, j in enumerate(keyList[(idxI if numsAmountMap[i] > 1 else idxI + 1):]):
                firstTwoSum = i + j
                if firstTwoSum > 0:
                    # print(2)
                    continue
                    # return outputList
                thirdNum = 0 - firstTwoSum
                idxJ = keyList.index(j)
                if thirdNum in keyList[(idxJ if numsAmountMap[j] > 1 else idxJ + 1):]:
                # if thirdNum in keyList[(idxI + idxJ if numsAmountMap[j] > 1 else idxI + idxJ + 1):]:
                    if (thirdNum == 0 and numsAmountMap[0] < 3) or (thirdNum == j and numsAmountMap[thirdNum] < 2):
                        # print('1')
                        # print(3)
                        break
                    # if (thirdNum == j and numsAmountMap[thirdNum] < 2) or (j > thirdNum):
                    #     print(4)
                        # break
                    # if (j > thirdNum):
                    #     break
                    outputList.append([i, j, thirdNum])
                    # print([i, j, thirdNum])

        return outputList

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1, -1, 2], [-1, 0, 1]]
    print(s.threeSum([-1,0,1,0])) # [[-1, 0, 1]]
    print(s.threeSum([3,0,-2,-1,1,2])) # [[-2,-1,3],[-2,0,2],[-1,0,1]]
    print(s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])) # [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

