"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def __init__(self):
        self.buttonMap = dict()
        asciiNumber = 97
        for n in range(0, 8):
            self.buttonMap[str(n + 2)] = list()
            for letter in range(0, 4 if n in (5, 7) else 3):
                self.buttonMap[str(n + 2)].append(chr(asciiNumber))
                asciiNumber += 1

    def outerJoinTwoList(self, lst1, lst2) -> list:
        outputList = list()
        for x in lst1:
            for y in lst2:
                outputList.append(x + y)
        return outputList

    def letterCombinations(self, digits: str) -> list[str]:
        if digits.__len__() >= 2:
            return self.outerJoinTwoList(
                self.buttonMap[digits[0]],
                self.letterCombinations(digits[1:])
            )
        elif digits.__len__() == 1:
            return self.buttonMap[digits]
        else:
            return []


if __name__ == '__main__':

    s = Solution()

    digits = "23"
    print(s.letterCombinations(digits))  # >> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    digits = ""
    print(s.letterCombinations(digits))  # >> []

    digits = "2"
    print(s.letterCombinations(digits))  # >> ["a","b","c"]

    print(s.buttonMap)