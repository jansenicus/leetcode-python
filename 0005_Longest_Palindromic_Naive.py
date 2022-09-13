class Solution:
    def longestPalindrome(self, s: str) -> str:
      """
      This is my naive bruteforce of Longest Palindromic Substring algorithm
      Where we check all possible combinations of substrings from a given string
      
      LeetCode Status: Time Limit Exceeded
      """
        
        def isPalindrome(s):
            """Return True if a string s is a palindrome"""
            return s[::] == s[::-1]


        def all_substrings(s):
            """Return all substrings from a given string"""
            all_subs = []
            for end in range(1, len(s) + 1):
                for start in range(end):
                    all_subs.append(s[start:end])
            return all_subs

        palindrome = {}
        for e in all_substrings(s):
            palindrome[e] = len(e) if isPalindrome(e) else 0

        return max(palindrome, key=palindrome.get)
