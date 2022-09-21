class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

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

        enums, enumt = {}, {}

        for e in s:

            if e in enums:
                enums[e] += 1
            else:
                enums[e] = 1

        for e in t:

            if e in enumt:
                enumt[e] += 1
            else:
                enumt[e] = 1

        return enums == enumt
