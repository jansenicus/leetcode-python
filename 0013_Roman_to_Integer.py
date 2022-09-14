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
        
        for k,v in roman2.items():
            if k in s:
                num += v
                s = s.replace(k,'')

        for e in s:
            num += roman1[e]

        return num
