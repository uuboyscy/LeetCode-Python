"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    """
    Runtime: 72 ms, faster than 5.55% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 13.7 MB, less than 98.66% of Python3 online submissions for Valid Parentheses.
    """
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            for p in ("()", "[]", "{}"):
                s = s.replace(p, "")
        return s.__len__() == 0

    """
    Runtime: 24 ms, faster than 98.89% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 14 MB, less than 44.15% of Python3 online submissions for Valid Parentheses.
    """
    def isValid(self, s: str) -> bool:
        symbolMap = {
            "(": 1,
            "[": 2,
            "{": 3,
            ")": -1,
            "]": -2,
            "}": -3
        }
        sList = list(s)  # List<String>
        stackList = [symbolMap[sList[0]]]  # List<Integer>

        for symbol in sList[1:]:
            isNewSymbolLtZero = symbolMap[symbol] < 0
            if isNewSymbolLtZero and stackList.__len__() == 0:
                stackList.append(symbolMap[symbol])
            elif isNewSymbolLtZero and symbolMap[symbol] + stackList[-1] == 0:
                del stackList[-1]
            elif isNewSymbolLtZero:
                return False
            else:
                stackList.append(symbolMap[symbol])

        return stackList == []

    def isValid(self, s: str) -> bool:
        symbol_map = {
            "(": 1,
            "[": 2,
            "{": 3,
            ")": -1,
            "]": -2,
            "}": -3
        }
        if s and (first_symbol := symbol_map[s[0]]) > 0:
            stack = [first_symbol]
        else:
            return False

        for symbol in s[1:]:
            if stack and symbol_map[symbol] + stack[-1] < 0:
                return False
            if stack and symbol_map[symbol] + stack[-1] > 0 and symbol_map[symbol] < 0:
                return False
            if stack and symbol_map[symbol] + stack[-1] == 0 and symbol_map[symbol] > 0:
                return False
            if stack and symbol_map[symbol] + stack[-1] == 0 and symbol_map[symbol] < 0 :
                stack.pop()
                continue

            stack.append(symbol_map[symbol])

        return stack == []


if __name__ == '__main__':
    s = Solution()

    print("()", s.isValid("()")) ## True
    print("()[]{}", s.isValid("()[]{}")) ## True
    print("(]", s.isValid("(]")) ## False
    print("()[{]}", s.isValid("()[{]}"))

