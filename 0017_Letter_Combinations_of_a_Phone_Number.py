class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
		
		Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

		A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

		Example 1:

		Input: digits = "23"
		Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
		Example 2:

		Input: digits = ""
		Output: []
		Example 3:

		Input: digits = "2"
		Output: ["a","b","c"]
		
		LC Runtime: 21 ms, faster than 78.46% of Python online submissions for Letter Combinations of a Phone Number.
		LC Memory Usage: 13.4 MB, less than 88.03% of Python online submissions for Letter Combinations of a Phone Number.
        """
        
        if(len(digits) == 0):
            return []

        chars = ['']

        phonebuttonmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        for d in digits:

            _ = []

            for letter in phonebuttonmap[d]:

            	for char in chars:
            		_.append(char+letter)

            chars = _

        return chars
        
