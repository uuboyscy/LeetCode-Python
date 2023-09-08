"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def greatest_common_divisor(a: int, b: int) -> int:
            if b == 0:
                return a
            else:
                return greatest_common_divisor(b, a % b)

        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[0 : greatest_common_divisor(len(str1), len(str2))]
