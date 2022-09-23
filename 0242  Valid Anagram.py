class Solution(object):
    def isAnagram(self, s, t):
        """
        https://leetcode.com/problems/valid-anagram/

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true
        Example 2:

        Input: s = "rat", t = "car"
        Output: false


        Constraints:

        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.


        Runtime: 41 ms, faster than 90.51% of Python online submissions for Valid Anagram.
        Memory Usage: 13.8 MB, less than 89.78% of Python online submissions for Valid Anagram.
        """

        enum_s, enum_t = {}, {}

        for e in s:

            if e in enum_s:
                enum_s[e] += 1
            else:
                enum_s[e] = 1

        for e in t:

            if e in enum_t:
                enum_t[e] += 1
            else:
                enum_t[e] = 1

        return enum_s == enum_t
