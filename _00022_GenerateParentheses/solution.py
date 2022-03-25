"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def insertBrackets(bkListArr: list[str]) -> list[str]:
            outputSet = set()
            bkStrListLen = bkListArr[0].__len__()
            for bkStr in bkListArr:
                bkStrList = list(bkStr)
                for i in range(0, bkStrListLen + 1):
                    bkStrList.insert(i, "()")
                    outputSet.add("".join(bkStrList))
                    bkStrList.pop(i)
            return list(outputSet)

        if n == 1:
            return ["()"]
        else:
            return insertBrackets(self.generateParenthesis(n - 1))


if __name__ == '__main__':
    s = Solution()

    n = 4
    print(n)
    print(s.generateParenthesis(n))  # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

    print("===")

    n = 3
    print(n)
    print(s.generateParenthesis(n))  # ["((()))","(()())","(())()","()(())","()()()"]

    print("===")

    n = 2
    print(n)
    print(s.generateParenthesis(n))  # ["()()", "(())"]

    print("===")

    n = 1
    print(n)
    print(s.generateParenthesis(n))  # ["()"]

    print("===")