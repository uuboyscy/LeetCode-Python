class Solution:
    def maxArea(self, height: list[int]) -> int:
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
    print(s.maxArea([1,1])) # 1
    print(s.maxArea([4,3,2,1,4])) # 16
    print(s.maxArea([1,2,1])) # 2