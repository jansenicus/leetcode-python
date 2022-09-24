class Solution:
    def isPalindrome(self, x: int) -> bool:
        """

        https://leetcode.com/problems/palindrome-number/

        Input: x = -121
        Output: false

        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
        Example 3:

        Input: x = 10
        Output: false

        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


        Constraints:

        -231 <= x <= 231 - 1

        Follow up: Could you solve it without converting the integer to a string?


        """
        x = str(x)                      # convert to string

        if '-' in x:                    # negative number is not a palindrome
            return False

        else:                           # non negative number may be a palindrome
            return x[::] == x[::-1]     # palindrome check
