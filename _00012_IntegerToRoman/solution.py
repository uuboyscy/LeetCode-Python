'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
'''

class Solution1:
    def intToRoman(self, num: int) -> str:
        PATTERNS = ["I", "V", "X", "L", "C", "D", "M"]
        n = str(num)
        def numberStrToRoman(n: str, p=0) -> str:
            if n.__len__() > 1:
                return numberStrToRoman(n[0:-1], p + 2) + numberStrToRoman(n[-1], p)
            else:
                number = int(n)
                if number <= 3:
                    return PATTERNS[p] * number
                elif number <= 4:
                    return PATTERNS[p] + PATTERNS[p + 1]
                elif number <= 8:
                    return PATTERNS[p + 1] + PATTERNS[p] * (number - 5)
                else:
                    return PATTERNS[p] + PATTERNS[p + 2]

        return numberStrToRoman(n)

if __name__ == "__main__":
    num = 3
    print(Solution1().intToRoman(num)) ## "III"

    num = 58
    print(Solution1().intToRoman(num))  ## "LVIII"

    num = 1994
    print(Solution1().intToRoman(num))  ## "MCMXCIV"