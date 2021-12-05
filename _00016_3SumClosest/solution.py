'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        numSet = set(nums)
        closestSum = 30000 if target >= 0 else -30000

        for fixNum in numSet:
            idxLeftNum = nums.index(fixNum) + 1
            idxRightNum = nums.__len__() - 1
            if idxLeftNum > nums.__len__() - 2: continue
            leftNum = nums[idxLeftNum]
            rightNum = nums[idxRightNum]
            while idxLeftNum < idxRightNum:
                threeSum = fixNum + leftNum + rightNum
                if threeSum == target:
                    return target
                elif threeSum < target:
                    idxLeftNum += 1
                elif threeSum > target:
                    idxRightNum -= 1
                leftNum = nums[idxLeftNum]
                rightNum = nums[idxRightNum]
                closestSum = threeSum if abs(threeSum - target) < abs(closestSum - target) else closestSum

        return closestSum

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1)) ## 2
    print(s.threeSumClosest([0,0,0], 1)) ## 0
