class Solution:
    def reverse(self, x: int) -> int:
        """
        https://leetcode.com/problems/reverse-integer/

        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

        Example 1:

        Input: x = 123
        Output: 321

        Example 2:

        Input: x = -123
        Output: -321

        Example 3:

        Input: x = 120
        Output: 21

        Constraints:

        -2**31 <= x <= 2**31 - 1

        Success Details:
        Best Runtime: 33 ms, faster than 94.29% of Python3 online submissions for Reverse Integer.

        """
        
        upper_limit = 2 ** 31 - 1                               # upper limit
        lower_limit = 1 - upper_limit                           # lower limit

        sgn = 1 if x > 0 else -1                                # sign + or -
        x = x * sgn                                             # sign * x
        rev = 0                                                 # placeholder for reverse int x
            
        while x:
            q, r = divmod(x, 10)                                # `q: quotient` and `r: remainder`
            x = q                                               # update `x` equals to `q`
            rev = rev * 10 + r                                  # update `rev` times ten + `r: remainder`

            if not lower_limit <= sgn*rev <= upper_limit:       # for value outside limit
                return 0                                        # return 0
            
        return sgn*rev                                          # final value of reverse int x
