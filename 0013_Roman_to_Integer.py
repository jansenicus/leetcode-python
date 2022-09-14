class Solution:
    def romanToInt(self, s: str) -> int:
      """
      Given a roman numeral, convert it to an integer.
      """

        roman1 = {
                  "M"   : 1000,
                  "D"   : 500,
                  "C"   : 100,
                  "L"   : 50,
                  "X"   : 10,
                  "V"   : 5,
                  "I"   : 1,
                }

        roman2 = {
                  "CM"  : 900,
                  "CD"  : 400,
                  "XC"  : 90,
                  "XL"  : 40,
                  "IV"  : 4,
                  "IX"  : 9
        }
        
        num = 0
        
        for k,v in roman2.items():                      # check roman2 table
            if k in s:                                  # if element exists in table
                num += v                                # accumulate the value
                s = s.replace(k,'')                     # remove the character

        for e in s:                                     # for each remaining character
            num += roman1[e]                            # translate and accumulate its value

        return num
