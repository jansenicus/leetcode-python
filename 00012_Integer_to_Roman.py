class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Integer to Roman
        
        Runtime: 38 ms, faster than 99.69% of Python3 online submissions for Integer to Roman.
        Memory Usage: 13.9 MB, less than 35.66% of Python3 online submissions for Integer to Roman.
        """
        roman = ""
        table = {
          "M"   : 1000,
          "CM"  : 900,
          "D"   : 500,
          "CD"  : 400,
          "C"   : 100,
          "XC"  : 90,
          "L"   : 50,
          "XL"  : 40,
          "X"   : 10,
          "IX"  : 9,
          "V"   : 5,
          "IV"  : 4,
          "I"   : 1,
        }
        
        for sym, val in table.items():
          d, m = divmod(num, val)
          roman += sym * d
          num = m
        
        return roman
