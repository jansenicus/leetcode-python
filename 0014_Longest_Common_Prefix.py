class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      """
      Write a function to find the longest common prefix string amongst an array of strings.

      If there is no common prefix, return an empty string "".

      Example 1:
      Input: strs = ["flower", "flow", "flight"]
      Output: "fl"
      
      Example 2:
      Input: strs = ["dog", "racecar", "car"]
      Output: ""
      Explanation: There is no common prefix among the input strings.


      Constraints:
      1 <= strs.length <= 200
      0 <= strs[i].length <= 200
      strs[i] consists of only lowercase English letters.
      """
        
        prefix = strs[0] if len(strs) else ""                   # initialize `prefix` equals to the first `strs`
        
        for i in range(1, len(strs)):
            
            char = ""                                           # initialize empty character
            word = strs[i]                                      # `word` equals current string
            
            if len(prefix) == 0:
                break
                
            for j in range(0, len(word)):                       # loop in the current `word`
                if j < len(prefix) and prefix[j] == word[j] :   # selection criteria 
                    char += prefix[j]                           # add `char` into prefix
                else:
                   break
                
            prefix = char
            
        return prefix
