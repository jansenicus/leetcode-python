class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        Example 1:

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        Example 2:

        Input: n = 1
        Output: ["()"]

        Constraints:

        1 <= n <= 8
        """

        ans = []

        def gen(left, right, s):

            if left == right == n:                  # stop when left = right = n
                ans.append(s)                       # `s` is the answer
                return

            if left < n:                            # if left < n
                gen(left + 1,                       # increase left
                    right,                          #
                    s + "(")                        # add left opening "("

            if right < left:                        # if right < left
                gen(left,                           #
                    right + 1,                      # increase right
                    s + ")")                        # add right closing ")"


        gen(0, 0, '')

        return ans
