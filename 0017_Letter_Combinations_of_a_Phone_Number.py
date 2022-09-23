class Solution(object):
    def letterCombinations(self, digits):
        """

        https://leetcode.com/problems/letter-combinations-of-a-phone-number/

        Given a string containing digits from 2-9 inclusive,
        return all possible letter combinations that the number could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below.
        Note that 1 does not map to any letters.

        Example 1:
        Input: digits = '23'
        Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']

        Example 2:
        Input: digits = ''
        Output: []

        Example 3:
        Input: digits = '2'
        Output: ['a','b','c']

        Success Details:
        Runtime: 23 ms, faster than 99.59% of Python3 online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 13.9 MB, less than 79.28% of Python3 online submissions for Letter Combinations of a Phone Number.

        """
        
        if len(digits) == 0:
            return []

        combinations = ['']

        phone_button = {
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

            _combinations = []

            for letter in phone_button[d]:

                for combination in combinations:

                    _combinations.append(combination+letter)

            combinations = _combinations

        return combinations
        
