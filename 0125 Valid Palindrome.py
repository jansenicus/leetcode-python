class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-palindrome/submissions/
        """
        cleanstring = ""

        for e in s:
                if e.isalnum():
                    cleanstring += e.lower()

        return cleanstring == cleanstring[::-1]