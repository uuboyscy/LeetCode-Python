'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x >= 2147483647 or x <= -2147483648:
            return 0
        tmpStr = str(x)[-1::-1]
        tmpStr = tmpStr if tmpStr[0] != '0' else tmpStr[1:]
        tmpStr = tmpStr if tmpStr[-1] != '-' else ('-' + tmpStr[:-1])
        outputInt = int(tmpStr)
        return 0 if (outputInt >= 2147483647 or outputInt <= -2147483648) else outputInt

class Solution2:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x >= 2147483647 or x <= -2147483648:
            return 0
        tmpStr = str(x)[-1::-1]
        tmpStr = tmpStr if tmpStr[0] != '0' else tmpStr[1:]
        tmpStr = tmpStr if tmpStr[-1] != '-' else ('-' + tmpStr[:-1])
        tmpStr = int(tmpStr)
        return 0 if (tmpStr >= 2147483647 or tmpStr <= -2147483648) else tmpStr

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(0))
    print('123'[-1::-1])
    print(2**31)
    print(1534236469)

