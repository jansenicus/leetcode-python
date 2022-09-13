class Solution:
    def reverse(self, x: int) -> int:
        """
        Given a signed 32-bit integer x, 
        return x with its digits reversed. 
        
        If reversing x causes the value to go 
        outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
        
        Assume the environment does not allow you to store 64-bit integers 
        (signed or unsigned).
        
        Best Runtime: 33 ms, faster than 94.29% of Python3 online submissions for Reverse Integer.
        """
        
        max_bound = 2 ** 31                                 # maximum bound
        sign = 1 if x > 0 else -1                           # sign + or -
        x = x * sign                                        # sign * x 
        r = 0                                               # placeholder for reverse int x
            
        while x:                                            # as x holds a non-zero value
            r, x = r * 10 + x % 10, x//10                   # recursive r and x
            if not - max_bound <= sign*r <= max_bound -1:
                return 0                                    # return 0 for value outside
            
        return sign*r                                       # final value of reverse int x
