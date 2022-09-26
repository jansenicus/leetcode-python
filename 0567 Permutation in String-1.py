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

        Success Details:
        Runtime: 72 ms, faster than 94.24% of Python3 online submissions for Permutation in String.
        Memory Usage: 14 MB, less than 68.12% of Python3 online submissions for Permutation in String.
        """
        #
        # this solution requires resultant freq == all zero
        # to confirm that a permutation of s1 exists in string s2
        #
        if len(s2) < len(s1):                       # impossible
            return False

        if s1 == s2:                                # edge case
            return True

        n1 = len(s1)                                # the length of s1
        freq = [0] * 26                             # `freq` array of length 26 will store frequency of each element

        def at_index(x):                            # `at_index` will return 0-25 for ASCII character `a-z`
            return ord(x) - ord('a')

        for _ in s1:                                # for each element in s1
            freq[at_index(_)] += 1                  # count frequency of every element as a reference counter

        for i, _ in enumerate(s2):

            freq[at_index(_)] -= 1                  # set negative frequency `-1` for each element in `s2`

            if i >= n1:                             # if index exceed the length of n1 = len(s1)
                ref = s2[i-n1]                      # look at reference element at `i-n1`
                freq[at_index(ref)] += 1            # set positive frequency `+1` for that element

            if not any(freq):                       # if the resultant of all `freq` is `0`
                return True                         # return True because we have a permutation match

        return False                                # otherwise False because we don't have a match
