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
        #
        # this solution requires matches == 26
        # to confirm that a permutation of s1 exists in string s2
        #

        if len(s2) < len(s1):
            return False
        if s1 == s2:
            return True

        freq1, freq2 = [0] * 26, [0] * 26                   # initialize 26 elements at value 0
        matches = 0                                         # init matches at value 0

        def at_index(x):                                    # `at_index` will return 0-25 for ASCII character `a-z`
            return ord(x) - ord('a')

        for _ in range(0, len(s1)):                         # loop in the length of `s1`
            freq1[at_index(s1[_])] += 1                     # once initialized `freq1` will be constant
            freq2[at_index(s2[_])] += 1                     # while `freq2` will be changing along the sliding window

        for _ in range(0, 26):
            matches += 1 if freq2[_] == freq1[_] else 0     # initialize `matches`

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:                               # if `matches` == 26 then we have got a match
                return True

            _ = at_index(s2[r])                             # check element at `r` pointer

            freq2[_] += 1                                   # increase `freq2` for incoming element

            if freq2[_] == freq1[_]:                        # if current element frequency matches
                matches += 1                                # `matches` += 1

            elif freq2[_] == freq1[_] + 1:                  # if the frequency mismatches
                matches -= 1                                # reduce `matches`

            _ = at_index(s2[l])                             # check element at `l` pointer

            freq2[_] -= 1                                   # reduce `freq` for outgoing element

            if freq2[_] == freq1[_]:                        # if current element frequency matches
                matches += 1                                # increase `matches`

            elif freq2[_] == freq1[_] - 1:                  # if the frequency mismatch
                matches -= 1                                # reduce `matches`

            l += 1                                          # increase `left` pointer

        return matches == 26                                # True if `matches` == 26
