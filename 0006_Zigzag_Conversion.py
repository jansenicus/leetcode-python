class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Runtime: 50 ms, faster than 98.45% 
        # inspired:
        # https://atharayil.medium.com/zigzag-conversion-day-71-python-e48744c51601
        # 
        if(numRows  == 1): return s         # edge case where numRows == 1
                                            # just return the string 's' as is
        Z = [''] * numRows                  # initialize Zigzag array
        top = 0                             # top is 0
        bottom = numRows - 1                # bottom is numRows - 1
        r = 0                               # initialize r = 0 as the first row
        way = -1                            # initialize direction
        
        for e in s:                         # for each element `e` in string `s`:
            Z[r] += e                       # put element e in Z[row] array
            if r == top or r == bottom:     # when row hit extremes (top/ bottom)
                 way *= -1                  # then flip the initial direction
            r = r + way                     # update row `r` accordingly

        return(''.join(Z))                  #return the Z array
        
