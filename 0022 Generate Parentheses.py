class Solution(object):
    def generateParenthesis(self, n):
        """
        https://leetcode.com/problems/generate-parentheses/
        https://youtu.be/s9fokUqJ76A

        Given n pairs of parentheses,
        write a function to generate all combinations of well-formed parentheses.

        Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        Example 2:
        Input: n = 1
        Output: ["()"]

        Constraints:

        1 <= n <= 8
        """

        parentheses = []                    # placeholder for all valid parentheses

        def gen(l, r, s):                   # recursive function to generate parentheses

            if l == r == n:                 # stop when left = right = n
                parentheses.append(s)       # `s` is the answer

            if l < n:                       # if left < n
                gen(l + 1, r, s + "(")      # add left opening "("

            if r < l:                       # if right < left
                gen(l, r + 1, s + ")")      # add right closing ")"


        gen(0, 0, '')

        return parentheses
