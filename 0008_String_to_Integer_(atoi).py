class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
        """
        s = s.strip()                   # strip any leading and trailing spaces
        regexp = r'[-+]?\d+'            # regex pattern for [-+]*\d+
        s = re.match(regexp, s)        	# match the regex pattern 
        if not s: return 0              # return 0 if no string

	maxint = 2147483647             
        minint = -2147483648
				
        if s:				# if there is a match then do several checks
            num = int(s.group())
            if num > maxint:		# if it is greater than maxint then return maxint
                return maxint
            elif num < minint:		# if is is lesser than minint then return minint
                return minint
            else:			# when all checks failed then return `num` as is
                return num
