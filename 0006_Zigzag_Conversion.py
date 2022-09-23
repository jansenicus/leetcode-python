class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        https://leetcode.com/problems/zigzag-conversion/

        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);


        Example 1:

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

        Example 2:

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"

        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I

        Example 3:

        Input: s = "A", numRows = 1
        Output: "A"


        Constraints:

        1 <= s.length <= 1000
        s consists of English letters (lower-case and upper-case), ',' and '.'.
        1 <= numRows <= 1000

        Success Details:
        Runtime: 50 ms, faster than 98.45%

        Discussion:
        https://atharayil.medium.com/zigzag-conversion-day-71-python-e48744c51601

        """
        if numRows == 1:                    # edge case where numRows == 1
            return s                        # just return the string 's' as is

        zigzag = [''] * numRows             # initialize Zigzag array with empty string
        top = 0                             # top is 0
        bottom = numRows - 1                # bottom is numRows - 1
        r = 0                               # initialize r = 0 as the first row
        way = -1                            # initialize direction
        
        for e in s:                         # for each element `e` in string `s`:

            zigzag[r] += e                  # put element e in Z[row] array

            if r == top or r == bottom:     # when row hit extremes (top/ bottom)
                way = -1* way               # then flip the initial direction

            r = r + way                     # update row `r` accordingly

        return ''.join(zigzag)              #return the Z array
        
