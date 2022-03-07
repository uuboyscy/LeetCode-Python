"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            for p in ("()", "[]", "{}"):
                s = s.replace(p, "")
        return s.__len__() == 0

    def isValid(self, s: str) -> bool:
        symbolMap = {
            "(": 1,
            "[": 2,
            "{": 3,
            ")": -1,
            "]": -2,
            "}": -3
        }
        sList = list(s)
        stackList = [symbolMap[sList[0]]]
        sSum = 0

        for symbol in sList[1:]:
            if symbolMap[symbol] < 0 and symbolMap[symbol] + stackList[-1] == 0:
                del stackList[-1]
            elif symbolMap[symbol] < 0:
                return False
            else:
                stackList.append(symbol)

        return stackList == []



if __name__ == '__main__':
    s = Solution()

    print(s.isValid("()")) ## True
    print(s.isValid("()[]{}")) ## True
    print(s.isValid("(]")) ## False
    print(s.isValid("()[{]}"))

