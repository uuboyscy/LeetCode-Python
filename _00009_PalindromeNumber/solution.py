'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        return xStr[::-1] == xStr

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(3))
    print(s.isPalindrome(30))
    print(s.isPalindrome(303))
    print(s.isPalindrome(-123))
    print(s.isPalindrome(121))

    print('123'[::-1])