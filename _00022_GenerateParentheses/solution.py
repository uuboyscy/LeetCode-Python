"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def insertOneBlucket(bkListArr: list[str]) -> list[str]:
            outputSet = set()
            for bkStr in bkListArr:
                outputSet.add("".join([bkStr] + ["(", ")"]))
                outputSet.add("".join(["(", ")"] + [bkStr]))
                outputSet.add("".join(["("] + [bkStr] + [")"]))
            return list(outputSet)

        if n == 1:
            return ["()"]
        else:
            # [bkStr.split("") for bkStr in self.generateParenthesis(n - 1)]
            return insertOneBlucket(self.generateParenthesis(n - 1))


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