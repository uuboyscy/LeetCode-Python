"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def containSubStr(self, s, pList):
        for subStr in pList:
            if s.__contains__(subStr):
                return True
        return False

    def isValid(self, s: str) -> bool:
        for p in ("()", "[]", "{}"):
            if self.containSubStr(s, ("()", "[]", "{}")):
                s = s.replace(p, "")



if __name__ == '__main__':
    s = Solution()

    print(s.isValid("()")) ## True
    print(s.isValid("()[]{}")) ## True
    print(s.isValid("(]")) ## False
    print("{{}}}}()}[]".__contains__(("{[[[", "{}")))
