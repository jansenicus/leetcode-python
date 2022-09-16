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
        
        prefix = strs[0] if len(strs) else ""			# initialize `prefix` equals to the first `strs`
        
        for i, word in enumerate(strs, 1):              	# enumerate `strs` from index 1
            
            maxlen = len(prefix)                        	# `maxlen` to be the len of previous prefix
            if maxlen == 0: break                       	# break from loop when `maxlen` is zero
				
            _ = ""                                      	# `_` temporary placeholder for prefix
                
            for j, e in enumerate(word):                	# loop for each element `e` in `word`
                
                if j < maxlen and e == prefix[j]:       	# if current element `e` equals previous prefix
                    _ += e                              	# add current element `e` into `_`
                else: break
                    
            prefix = _
            
        return prefix
