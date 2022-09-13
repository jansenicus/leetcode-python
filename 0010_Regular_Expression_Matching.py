class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Given an input string s and a pattern p, 
        implement regular expression matching with 
        support for '.' and '*' where:
        
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        """
        
        pattern = re.compile(rf"{p}")         # rf : regular expression format string specifier
        return pattern.fullmatch(s)           # do a fullmatch
        
        """
        Runtime: 60 ms, faster than 80.20% of Python3 online submissions for Regular Expression Matching.
        Memory Usage: 13.9 MB, less than 90.82% of Python3 online submissions for Regular Expression Matching.
        """
