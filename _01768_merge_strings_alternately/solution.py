"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        output_str = ""

        for idx in range(min(len(word1), len(word2))):
            output_str += word1[idx]
            output_str += word2[idx]

        idx += 1
        output_str += word1[idx:] if len(word1) > len(word2) else word2[idx:]

        return output_str
