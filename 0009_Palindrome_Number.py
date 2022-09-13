class Solution:
    def isPalindrome(self, x: int) -> bool:
		"""
		Given an integer x, return true if x is palindrome integer.
		An integer is a palindrome when it reads the same backward as forward.
		For example, 
		121 is a palindrome while -121 is not because from left to right, it reads -121. 
		From right to left, it becomes 121-.
		"""
      
        x = str(x)								# convert to string
        if '-' in x: return False				# return False if '-' in str(x)
        return x[::] == x[::-1]					# palindrome definition
		
