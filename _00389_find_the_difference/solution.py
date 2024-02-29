"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def get_word_count_dict(input_string: str) -> dict[str, int]:
            word_count_dict = {}
            for word in input_string:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
            return word_count_dict

        wc_s = get_word_count_dict(s)
        wc_t = get_word_count_dict(t)

        for k, v in wc_t.items():
            if v > wc_s.get(k, 0):
                return k



if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))

    s = ""
    t = "y"
    print(Solution().findTheDifference(s, t))

    s = "a"
    t = "aa"
    print(Solution().findTheDifference(s, t))