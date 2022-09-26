class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        https://leetcode.com/problems/permutation-in-string/
        https://youtu.be/UbyhOgBN834

        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
        In other words, return true if one of s1's permutations is the substring of s2.

        Example 1:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").

        Example 2:
        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false

        Constraints:
        1 <= s1.length, s2.length <= 104
        s1 and s2 consist of lowercase English letters.
        """
        # comparing counter of the sliding window with reference
        #
        from collections import Counter
        reference = Counter(s1)                     # counter of every element in s1

        if len(s2) < len(s1):                       # impossible
            return False

        if s1 == s2:                                # edge case
            return True

        for i in range(0, len(s2) - 1):

            window = s2[i: i + len(s1)]             # sliding window

            if Counter(window) == reference:        # check Counter window equals the reference
                return True

        return False                                # return False if no match found
