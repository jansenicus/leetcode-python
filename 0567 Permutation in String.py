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
        # comparing counter of the slice with reference
        #
        # from collections import Counter
        # reference = Counter(s1)
        #
        # if len(s2) < len(s1):
        #     return False
        #
        # if s1 == s2:
        #     return True
        #
        # for i in range(0, len(s2) - 1):
        #
        #     slice = s2[i: i + len(s1)]
        #
        #     if Counter(slice) == reference:
        #         return True
        #
        # return False

        if len(s2) < len(s1):
            return False
        if s1 == s2:
            return True

        ref, counter = [0] * 26, [0] * 26                       # initialize 26 elements at value 0
        matches = 0                                             # init matches at value 0
        at_index = lambda l: ord(l) - ord('a')                  # `at_index` return 0-26

        for _ in range(0, len(s1)):                             # populate `ref` and `counter`
            ref[ at_index( s1[_]) ] += 1                        # populate `ref`
            counter[ at_index( s2[_] ) ] += 1                   # count element and update `counter`

        for _ in range(0, 26):
            matches += 1 if counter[_] == ref[_] else 0         # populate `matches`

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            _ = at_index(s2[r])                                 # element to check for new match

            counter[_] += 1                                     # increase `counter`
            if counter[_] == ref[_]:
                matches += 1                                    # increase `matches`

            elif counter[_] == ref[_] + 1:
                matches -= 1                                    # reduce `matches`

            _ = at_index(s2[l])                                 # element to check for match

            counter[_] -= 1                                     # reduce `counter`
            if counter[_] == ref[_]:
                matches += 1                                    # increase `matches`

            elif counter[_] == ref[_] - 1:                      #
                matches -= 1                                    # reduce `matches`

            l += 1
        return matches == 26